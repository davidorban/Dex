---
name: librarian
description: Proactive research librarian. Hybrid lex+vec search over 1,377 PDFs in 06-Resources/Research/ with page-accurate citations. Run /librarian "<query>" to surface relevant passages while drafting.
model_hint: standard
---

Two-phase tool: (1) **ingest** — turn the PDF library into a per-page markdown cache QMD can index; (2) **query** — hybrid lex+vec search with page-level citations.

## Usage

- `/librarian "<query>"` — Search the research library. Returns top 5 hits with `File.pdf:p.N` citations and 2-line snippets.
- `/librarian ingest [--full|--incremental|--dry-run|--clean]` — Refresh the index. Run after adding PDFs.

## Arguments

- `$ARG1`: the query string (for default search mode) OR `ingest` (to trigger pipeline)
- Additional args after `ingest`: pass through to `scripts/ingest.py`

## Behavior on `/librarian "<query>"`

1. Activate the venv: `source /tmp/librarian-venv/bin/activate`
2. Call the QMD MCP directly when invoked by Claude: `mcp__qmd-mcp__query` with:
   - `searches=[{"type":"lex","query":"<query>"},{"type":"vec","query":"<query>"}]`
   - `collection="research"`
   - `limit=5`
   - `intent="research-pdf-citation-lookup"`
3. For each hit, parse the file path `.derived/<rel-pdf-stem>/p<NNNN>.md` to extract:
   - **page number** = `NNNN` (zero-padded)
   - **source PDF** = `06-Resources/Research/<rel-pdf-stem>.pdf`
4. Format output as a clean list of citations:
   ```
   1. **<filename>.pdf**:p.<N>  (score 0.XX)
      > <snippet, single line, ≤320 chars>
   ```
5. Suggest the user paste the bold lines into their draft.

CLI fallback (when not running inside Claude): `python .claude/skills/librarian/scripts/query.py "<query>"` — same logic via the `qmd` binary.

## Behavior on `/librarian ingest`

1. Activate the venv.
2. Run `python .claude/skills/librarian/scripts/ingest.py <args>` — defaults to `--incremental` (sha1-skip).
3. Report the summary line (processed / skipped / failures / total pages / wall time).
4. If failures > 0, point at `06-Resources/Research/.derived/_failures.json` for the per-PDF reason list.
5. Trigger QMD reindex of the `research` collection (manual or via `mcp__qmd-mcp__reindex`).

## Pre-flight (one-time)

```bash
python3 -m venv /tmp/librarian-venv
source /tmp/librarian-venv/bin/activate
pip install pypdf tqdm 'cryptography>=3.1' pytest
```

The `cryptography>=3.1` constraint matters — pypdf needs it to decrypt AES-encrypted PDFs. Without it, ~38 PDFs in the active research library silently fail with `pypdf open failed: cryptography>=3.1 is required for AES algorithm`. If you see that error in `_failures.json`, the venv install didn't include cryptography (verify with `pip show cryptography`).

Tests (run after any code change):

```bash
cd /Users/davidorban/Dev/Dex/.claude/skills/librarian
python -m pytest tests/ -v
```

## Files

- `scripts/ingest.py` — page-per-file PDF→markdown pipeline (v2). Atomic writes, sha1 idempotency, taxonomy validation, per-PDF metadata sidecars.
- `scripts/query.py` — CLI hybrid search via the qmd binary; parses page numbers from file paths.
- `scripts/_categories.py` — canonical subject taxonomy (validated against the User Guide).
- `tests/` — pytest cases for taxonomy + sha1 + path helpers.

## Output layout (v2 page-per-file format)

```
06-Resources/Research/.derived/
├── _manifest.json                    # global sha1 cache (per-PDF entries)
├── _failures.json                    # last run's failed-PDF list
└── <Subject>/<Geography>/<PDFstem>/
    ├── _meta.json                    # per-PDF metadata sidecar (NOT indexed)
    ├── p0001.md                      # pure page content (NO frontmatter)
    ├── p0002.md
    └── ...
```

Why pure-content `.md` files: the previous frontmatter-embedded format leaked sha1 hashes, source paths, and ingestion timestamps into QMD search snippets. The metadata now lives in `_meta.json` (excluded from indexing by the `_` prefix convention).

Why one file per page: page numbers come from the filename, not from parsing snippets. This is the only reliable way to cite `File.pdf:p.N` accurately when the matched chunk might span page boundaries.

## Known gotchas

1. **Encrypted PDFs** — pypdf attempts an empty-password decrypt; PDFs with real passwords land in `_failures.json` as `encrypted:`. Manual unlock required.
2. **Chinese / RTL filenames** — preserved as-is; QMD indexes them but case folding may behave oddly. Spot-check after ingest.
3. **39 baseline failures** — most are in `ZZ Archived Structure/` (legacy folder). Acceptable to leave; the active categories have <10 failures.
4. **QMD reindex** — after `ingest`, QMD doesn't see new content until the daily reindex runs. Trigger manually via `mcp__qmd-mcp__reindex` for immediate visibility.
5. **Format migration** — moving from v1 (per-PDF .md with frontmatter) to v2 (per-page directory tree) requires `--clean --full`. Old `.derived/` content must be deleted first.

## References

- Master plan: `plans/dex-improvement-proactive-librarian.md`
- 5 ADRs: `docs/adr/ADR-001` through `ADR-005`
- Execution log: `docs/proactive-librarian/Phase-1-Foundation-Execution-Log.md`
- Recipe: `06-Resources/Recipe_Library/01-AI-improves-research-citation.md`
