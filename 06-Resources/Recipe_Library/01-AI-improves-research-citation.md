# Recipe: AI Improves Research Citation — Proactive Librarian

> **🆕 New in Dex v1.20 (May 2026)**  
> The Proactive Librarian is now available. Run `/librarian "your query"` to get instant, page-accurate citations from your entire 1,377-PDF research library.

**Date:** 2026-05-16  
**Author:** David Orban  
**Pillar:** Change & Knowledge Management (R2) + Al Liwan Labs (R3)  
**Goal Alignment:** Q2-2026 Goal 4 — "AI improves [X]" recipe library (Recipe #1)

---

## The Problem (Before)

When writing memos, briefs, decks, or strategy documents, I frequently needed to cite research PDFs from my library of 1,377 documents (~11 GB) in `06-Resources/Research/`.

**Previous workflow:**
- Folder/filename grep (slow, brittle, depends on remembering where a report lived)
- Opening PDFs one by one with Ctrl+F
- Often couldn't recall which report contained the specific data point
- No quick path to **page-level citations**

The friction was high enough that I'd often cite vaguely (or not at all) rather than dig.

---

## The Solution (After)

I built the **Proactive Librarian** — a Dex skill that lets me run:

```bash
/librarian "stablecoin regulation in emerging markets"
```

And get back the top relevant passages with **precise page citations** I can paste directly into my document.

**New workflow:**
1. Type a natural language query in any context
2. Get ranked results with `File.pdf:p.XX` citations
3. Paste the citation + excerpt into my deliverable
4. Click the link in Obsidian/Preview to jump straight to the page

Query latency is under 30 seconds end-to-end (hybrid lex+vec search). The wall-clock improvement vs. the previous folder-grep workflow is substantial but hasn't been formally benchmarked — the qualitative shift (citation becomes the default behaviour, not the exception) is the real win.

---

## Tools & Stack Used

| Layer | Tool | Purpose |
|-------|------|---------|
| **Ingestion** | `pypdf` + custom Python pipeline | Per-page text extraction with `## Page N` markers |
| **Storage** | QMD (local hybrid search) | BM25 + vector search over 27k+ chunks |
| **Interface** | Dex skill (`/librarian`) | Simple slash command surface |
| **Architecture** | No new MCP server | Reused existing QMD + Dex skill pattern |

**Key design decisions** (documented in ADRs):
- PDF is canonical; derived markdown is a reproducible cache
- Page-level granularity (not paragraph or file-level)
- Explicit invocation only (v1)
- QMD as the retrieval substrate (no new vector database)

---

## How to Replicate This Pattern

This recipe is now reusable for any large document collection.

### 1. Ingest Pipeline Pattern
- Walk source files (PDFs, DOCX, etc.)
- Extract with structure preservation (page numbers, sections)
- Write derived markdown with consistent markers (`## Page N`)
- Store rich frontmatter (source, category, sha1, etc.)
- Make it idempotent on content hash

### 2. Retrieval Layer Pattern
- Add a dedicated QMD collection pointed at the derived folder
- Use hybrid queries (`lex:` + `vec:`) for best results
- Parse structural markers from results to surface citations

### 3. Interface Pattern
- Expose via a simple Dex skill (`/librarian "query"`)
- Return clean, copy-pasteable output with citations
- Follow the existing expense-report / triage skill shape

---

## Results

| Dimension | Before | After |
|---|---|---|
| Citation precision | Vague (e.g., "in a McKinsey report") | Specific (`File.pdf:p.12`) |
| Friction to cite research | High — often skipped | Low — now the default behaviour |
| Derived cache size | n/a | 132 MB across the page-per-file tree |
| Query latency | minutes to hours of manual search | sub-30-second hybrid retrieval |

**Qualitative wins:**
- I cite research *more often* because the friction collapsed.
- Citations are more credible because they include the page.
- The system surfaces reports I had forgotten existed.

**Honest caveats:**
- The "before" timing range was never instrumented; it's a recollection, not a measurement.
- Page-number accuracy depends on PDF extraction quality (image-only or heavily formatted PDFs may misreport).
- 39 of 1,377 PDFs failed ingest on the first pass (mostly encrypted or in the legacy `ZZ Archived Structure/` folder). See `06-Resources/Research/.derived/_failures.json`.

---

## Reusable Template

This pattern ("AI improves research citation") can be applied to:

- Legal document libraries
- Academic paper collections
- Internal company research repositories
- Policy and regulatory document sets

**Core reusable components:**
- Per-page (or per-section) markdown extraction with structural markers
- Dedicated QMD collection + hybrid search
- Simple skill interface returning citable excerpts

---

## Lessons Learned

1. **Page-level granularity was the right call** — file-level search would have been much less useful.
2. **Real data is messy** — encrypted PDFs, poor text extraction, and weird folder naming were bigger issues than the AI components.
3. **The recipe template is powerful** — forcing myself to document this as a reusable pattern made the work more valuable than a one-off tool.
4. **QMD was the correct substrate** — adding a new vector database would have added unnecessary complexity for this scale.

---

## References

- Master Plan: `plans/dex-improvement-proactive-librarian.md`
- ADRs: `docs/adr/ADR-001` through `ADR-005`
- Implementation Log: `docs/proactive-librarian/Phase-1-Foundation-Execution-Log.md`
- Scripts: `.claude/skills/librarian/scripts/`

**This is Recipe #1 in the Q2-2026 "AI improves [X]" series.**