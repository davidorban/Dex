#!/usr/bin/env python3
"""ingest.py — PDF → per-page markdown pipeline for the Proactive Librarian.

v2 — page-per-file format (Phase 2.1, fixes #1 + #2 from review):
- Each PDF page is its own .md file at `.derived/<rel-pdf-stem>/p<NNN>.md`.
- .md files are PURE CONTENT (no frontmatter) so QMD doesn't index metadata.
- Per-PDF metadata lives in `<rel-pdf-stem>/_meta.json` (not indexed by QMD).
- Global `.derived/_manifest.json` keyed by relative PDF path for fast sha1 lookup.
- Per-run `.derived/_failures.json` surfaces every PDF that didn't ingest.

Architecture goals (documented for Claude + code-reviewer):
- Idempotent on file content (sha1). Re-runs are cheap.
- Atomic writes: never leave a half-written .md file.
- Loud, actionable failures on taxonomy violations.
- Page number is a property of the FILE PATH, never parsed from snippets.
- Zero side-effects on canonical PDFs (ADR-004).

Usage:
    source /tmp/librarian-venv/bin/activate
    python .../librarian/scripts/ingest.py --help
    python .../librarian/scripts/ingest.py --dry-run --limit 10
    python .../librarian/scripts/ingest.py --incremental   # default
    python .../librarian/scripts/ingest.py --full          # force re-extract everything
    python .../librarian/scripts/ingest.py --clean         # nuke .derived/ first (format migration)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

try:
    from pypdf import PdfReader
    from pypdf.errors import PdfReadError
    from tqdm import tqdm
except ImportError as e:
    print(
        "Missing dependency. Please run the pre-flight from SKILL.md:\n"
        "  python3 -m venv /tmp/librarian-venv\n"
        "  source /tmp/librarian-venv/bin/activate\n"
        "  pip install pypdf tqdm cryptography\n"
        f"\nOriginal error: {e}"
    )
    sys.exit(1)

from _categories import derive_subject_geography, validate_subject_or_raise

# =============================================================================
# CONSTANTS
# =============================================================================

RESEARCH_ROOT = Path("/Users/davidorban/Dev/Dex/06-Resources/Research")
DERIVED_ROOT = RESEARCH_ROOT / ".derived"
DERIVED_VERSION = 2  # bumped — page-per-file format
MANIFEST_PATH = DERIVED_ROOT / "_manifest.json"
FAILURES_PATH = DERIVED_ROOT / "_failures.json"


# =============================================================================
# DATA TYPES
# =============================================================================

@dataclass
class IngestStats:
    processed: int = 0
    skipped: int = 0
    errors: int = 0
    total_pages: int = 0
    failures: list[dict] = field(default_factory=list)

    def record_failure(self, pdf_path: Path, reason: str) -> None:
        self.errors += 1
        try:
            rel = str(pdf_path.relative_to(RESEARCH_ROOT))
        except ValueError:
            rel = str(pdf_path)
        self.failures.append({"pdf": rel, "reason": reason})


# =============================================================================
# CORE HELPERS
# =============================================================================

def compute_sha1(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Streaming SHA-1 — never loads the whole file."""
    h = hashlib.sha1()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()


def get_page_dir(pdf_path: Path) -> Path:
    """Map `Research/Foo/Bar.pdf` → `.derived/Foo/Bar/`."""
    rel = pdf_path.relative_to(RESEARCH_ROOT)
    return DERIVED_ROOT / rel.with_suffix("")


def page_filename(n: int) -> str:
    """Zero-pad page numbers so filesystem and QMD sort them in order."""
    return f"p{n:04d}.md"


def load_manifest() -> dict[str, dict]:
    """Return the global sha1-keyed manifest, or {} if absent."""
    if not MANIFEST_PATH.exists():
        return {}
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_manifest(manifest: dict[str, dict]) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = MANIFEST_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(MANIFEST_PATH)


def save_failures(stats: IngestStats) -> None:
    FAILURES_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_failures": len(stats.failures),
        "failures": stats.failures,
    }
    tmp = FAILURES_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    tmp.replace(FAILURES_PATH)


def extract_page_text(page) -> str:
    """Robust page extraction with graceful degradation.

    Sanitises unpaired UTF-16 surrogates (sometimes leak through from PDFs
    with emoji or 4-byte characters) by replacing them with U+FFFD —
    without this the .md write fails with 'surrogates not allowed'.
    """
    try:
        text = page.extract_text() or ""
    except Exception as exc:
        text = f"[pypdf extraction failed: {exc}]"
    # Strip unpaired surrogates that would crash utf-8 encode
    text = text.encode("utf-8", errors="replace").decode("utf-8")
    return text.strip()


def write_meta(page_dir: Path, source_pdf: Path, subject: str,
               geography: Optional[str], page_count: int,
               file_size: int, sha1: str) -> None:
    """Per-PDF metadata sidecar. Lives next to page files but is NOT indexed
    by QMD (filename starts with `_`)."""
    meta = {
        "source_pdf": str(source_pdf.relative_to(RESEARCH_ROOT)),
        "subject": subject,
        "geography": geography or "General",
        "page_count": page_count,
        "file_size_bytes": file_size,
        "sha1": sha1,
        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "derived_version": DERIVED_VERSION,
    }
    meta_path = page_dir / "_meta.json"
    tmp = meta_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    tmp.replace(meta_path)


def write_page(page_dir: Path, page_num: int, text: str) -> None:
    """Atomic write of a single-page pure-content .md."""
    path = page_dir / page_filename(page_num)
    tmp = path.with_suffix(".md.tmp")
    tmp.write_text(text + "\n", encoding="utf-8")
    tmp.replace(path)


def ingest_one(pdf_path: Path, manifest: dict[str, dict], force: bool,
               stats: IngestStats) -> str:
    """Process one PDF. Returns a short status string for progress UX."""
    rel_key = str(pdf_path.relative_to(RESEARCH_ROOT))

    try:
        subject, geography = derive_subject_geography(pdf_path)
        validate_subject_or_raise(subject)
    except ValueError as ve:
        stats.record_failure(pdf_path, f"taxonomy: {ve}".splitlines()[0])
        return "taxonomy-error"

    sha1 = compute_sha1(pdf_path)

    # Idempotency — skip if sha1 matches recorded manifest entry AND files exist
    page_dir = get_page_dir(pdf_path)
    prior = manifest.get(rel_key)
    if not force and prior and prior.get("sha1") == sha1 and page_dir.exists():
        stats.skipped += 1
        return "sha1-match"

    # Clear stale page files if this PDF was previously ingested
    if page_dir.exists():
        shutil.rmtree(page_dir)
    page_dir.mkdir(parents=True, exist_ok=True)

    try:
        reader = PdfReader(str(pdf_path))
        if reader.is_encrypted:
            try:
                if reader.decrypt("") == 0:
                    raise PdfReadError("PDF is encrypted with a non-empty password")
            except Exception as exc:
                stats.record_failure(pdf_path, f"encrypted: {exc}")
                shutil.rmtree(page_dir, ignore_errors=True)
                return "encrypted"
        page_count = len(reader.pages)
    except Exception as exc:
        stats.record_failure(pdf_path, f"pypdf open failed: {exc}")
        shutil.rmtree(page_dir, ignore_errors=True)
        return "open-error"

    try:
        for i, page in enumerate(reader.pages, start=1):
            text = extract_page_text(page)
            write_page(page_dir, i, text)
        write_meta(page_dir, pdf_path, subject, geography,
                   page_count, pdf_path.stat().st_size, sha1)
    except Exception as exc:
        stats.record_failure(pdf_path, f"page-write failed: {exc}")
        shutil.rmtree(page_dir, ignore_errors=True)
        return "write-error"

    manifest[rel_key] = {
        "sha1": sha1,
        "subject": subject,
        "geography": geography or "General",
        "page_count": page_count,
        "ingested_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    stats.processed += 1
    stats.total_pages += page_count
    return f"ingested {page_count}p"


# =============================================================================
# CLI
# =============================================================================

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Proactive Librarian PDF ingest (v2 — page-per-file)")
    p.add_argument("--full", action="store_true",
                   help="Ignore manifest sha1 cache; re-extract every PDF")
    p.add_argument("--incremental", action="store_true", default=True,
                   help="Default mode: only process new or sha1-changed PDFs")
    p.add_argument("--dry-run", action="store_true",
                   help="Walk + validate + sha1 but write nothing")
    p.add_argument("--limit", type=int, default=0,
                   help="Process at most N PDFs (useful for testing)")
    p.add_argument("--category", type=str, default=None,
                   help="Only process PDFs under this exact top-level subject")
    p.add_argument("--clean", action="store_true",
                   help="Delete .derived/ first (use for format migrations)")
    p.add_argument("--verbose", "-v", action="store_true",
                   help="Print every file decision")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if not RESEARCH_ROOT.exists():
        print(f"FATAL: Research root does not exist: {RESEARCH_ROOT}")
        sys.exit(2)

    if args.clean and DERIVED_ROOT.exists():
        print(f"--clean: removing {DERIVED_ROOT} ...")
        shutil.rmtree(DERIVED_ROOT)

    DERIVED_ROOT.mkdir(exist_ok=True)

    print("Scanning for PDFs under 06-Resources/Research/ ...")
    all_pdfs = sorted(p for p in RESEARCH_ROOT.rglob("*.pdf")
                      if ".derived" not in p.parts)
    print(f"Found {len(all_pdfs)} PDF files.")

    if args.category:
        all_pdfs = [p for p in all_pdfs
                    if derive_subject_geography(p)[0] == args.category]
        print(f"Filtered to {len(all_pdfs)} under category {args.category!r}.")

    if args.limit and args.limit > 0:
        all_pdfs = all_pdfs[: args.limit]
        print(f"Limited to first {len(all_pdfs)} PDFs.")

    if not all_pdfs:
        print("Nothing to do.")
        return

    print(f"Mode: {'FULL (force re-extract)' if args.full else 'INCREMENTAL (sha1 cache)'}")
    if args.dry_run:
        print("*** DRY RUN — no files will be written ***")

    manifest = load_manifest()
    stats = IngestStats()
    start = time.time()

    for pdf_path in tqdm(all_pdfs, desc="Ingesting", unit="pdf"):
        if args.dry_run:
            try:
                subject, _ = derive_subject_geography(pdf_path)
                validate_subject_or_raise(subject)
                stats.processed += 1
                if args.verbose:
                    tqdm.write(f"DRY ok: {pdf_path.relative_to(RESEARCH_ROOT)}")
            except ValueError as ve:
                stats.record_failure(pdf_path, str(ve).splitlines()[0])
            continue

        status = ingest_one(pdf_path, manifest, args.full, stats)
        if args.verbose:
            tqdm.write(f"{status}: {pdf_path.relative_to(RESEARCH_ROOT)}")

    elapsed = time.time() - start

    if not args.dry_run:
        save_manifest(manifest)
    save_failures(stats)

    print("\n" + "=" * 60)
    print("INGEST COMPLETE")
    print(f"  PDFs processed:         {stats.processed}")
    print(f"  PDFs skipped (sha1):    {stats.skipped}")
    print(f"  Failures:               {stats.errors}")
    print(f"  Total pages extracted:  {stats.total_pages}")
    print(f"  Wall time:              {elapsed:.1f}s ({elapsed/60:.1f} min)")
    print(f"  Derived cache:          {DERIVED_ROOT}")
    print(f"  Manifest:               {MANIFEST_PATH}")
    print(f"  Failures log:           {FAILURES_PATH}")
    print("=" * 60)

    if stats.errors > 0:
        print(f"\n{stats.errors} PDF(s) failed — inspect {FAILURES_PATH.name} for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
