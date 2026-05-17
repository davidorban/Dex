#!/usr/bin/env python3
"""query.py — Retrieval engine for the Proactive Librarian.

v2 — page-per-file (Phase 2.1):
- Pages live at `.derived/<rel-pdf-stem>/p<NNNN>.md`.
- The page number is parsed from the FILE PATH (not from snippets — that
  was unreliable and surfaced p.1 for everything).
- The source PDF path is derived from the parent directory.

Usage (CLI):
    source /tmp/librarian-venv/bin/activate
    python query.py "stablecoin regulation in the UAE" --limit 5
    python query.py "agentic AI in finance" --json

The `/librarian` slash command (see SKILL.md) calls Claude's `mcp__qmd-mcp__query`
tool directly, then formats the results using the same page-and-file extraction
logic documented here. This script remains the CLI fallback.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional


PAGE_FNAME_RE = re.compile(r"/p(\d+)\.md$", re.IGNORECASE)
QMD_URI_RE = re.compile(r"qmd://research/(.+)")


def find_qmd_binary() -> Optional[str]:
    """Locate the qmd CLI binary. Returns None if absent."""
    explicit = "/Users/davidorban/.bun/bin/qmd"
    if Path(explicit).exists():
        return explicit
    return shutil.which("qmd")


def run_qmd_hybrid_query(query: str, collection: str = "research",
                         limit: int = 5) -> list[dict[str, Any]]:
    """Execute a hybrid (lex + vec) query against the research collection.

    Returns parsed JSON results, or [] on failure.
    """
    qmd = find_qmd_binary()
    if qmd is None:
        print("qmd binary not found on PATH or at /Users/davidorban/.bun/bin/qmd",
              file=sys.stderr)
        return []

    structured = f"lex: {query}\nvec: {query}"
    cmd = [qmd, "query", structured,
           "--collection", collection,
           "--json",
           "-n", str(limit),
           "--min-score", "0.0"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True,
                                timeout=30, check=True)
        data = json.loads(result.stdout)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("results", [])
        return []
    except subprocess.CalledProcessError as e:
        print(f"qmd query failed (rc={e.returncode}): {e.stderr}", file=sys.stderr)
        return []
    except json.JSONDecodeError:
        print("Failed to parse qmd JSON output", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Unexpected error calling qmd: {e}", file=sys.stderr)
        return []


def parse_result_path(result: dict[str, Any]) -> tuple[Optional[str], Optional[int]]:
    """From a QMD result, return (source_pdf_relative_path, page_number).

    The page lives at `.derived/<rel-pdf-stem>/pNNNN.md`. We:
    - Strip any `qmd://research/` prefix.
    - Parse the trailing `/pNNNN.md` for the page number.
    - Drop the page file from the path and append `.pdf` to recover the original.

    Returns (None, None) if the path doesn't match the expected layout —
    callers should treat that as a malformed/legacy result.
    """
    raw = (result.get("file") or result.get("path") or "").strip()
    if not raw:
        return None, None

    m = QMD_URI_RE.search(raw)
    rel = m.group(1) if m else raw

    page_match = PAGE_FNAME_RE.search(rel)
    if not page_match:
        return None, None

    page = int(page_match.group(1))
    parent = rel[: page_match.start()]
    pdf_rel = parent + ".pdf"
    return pdf_rel, page


def format_citation(result: dict[str, Any]) -> str:
    """Turn a single QMD result into a clean, copy-pasteable citation."""
    snippet = (result.get("snippet") or "").strip()
    score = result.get("score", 0.0)

    pdf_rel, page = parse_result_path(result)
    label = Path(pdf_rel).name if pdf_rel else "Unknown.pdf"

    if page is not None:
        header = f"**{label}**:p.{page}  (score {score:.2f})"
    else:
        header = f"**{label}**  (score {score:.2f})"

    snippet = re.sub(r"\s+", " ", snippet).strip()
    if len(snippet) > 320:
        snippet = snippet[:317] + "..."

    return f"{header}\n> {snippet}\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Proactive Librarian — research PDF retrieval (CLI)")
    parser.add_argument("query", type=str,
                        help="Natural language query")
    parser.add_argument("--limit", "-n", type=int, default=5,
                        help="Max results (default 5)")
    parser.add_argument("--collection", default="research",
                        help="QMD collection to search")
    parser.add_argument("--json", action="store_true",
                        help="Raw JSON output (for scripting)")
    args = parser.parse_args()

    # Over-fetch then filter so we still return `limit` valid v2 hits even when
    # QMD's index still carries a few stale v1 .md entries (cleared by next reindex)
    raw = run_qmd_hybrid_query(args.query, args.collection, args.limit * 3)
    results = [r for r in raw if parse_result_path(r)[1] is not None][: args.limit]

    if not results:
        if raw:
            print("Found results but none in v2 page format — QMD index may be stale. "
                  "Run mcp__qmd-mcp__reindex and retry.")
        else:
            print("No results found (or qmd unavailable).")
        sys.exit(0)

    if args.json:
        # Re-shape with parsed page/pdf info for downstream consumers
        enriched = []
        for r in results:
            pdf_rel, page = parse_result_path(r)
            enriched.append({**r, "_pdf_rel": pdf_rel, "_page": page})
        print(json.dumps({"query": args.query, "results": enriched}, indent=2))
        return

    print(f'\nTop {len(results)} results for: "{args.query}"\n' + "=" * 60 + "\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. {format_citation(r)}")
        print("-" * 40)
    print("\nTip: paste the bold lines into your draft.")


if __name__ == "__main__":
    main()
