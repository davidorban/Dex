# Obsidian Enhancements

Reference for the Obsidian-side tooling layered on top of Dex. Installed and configured 2026-05-15. All pieces are designed to coexist safely with Dex automation — none of them auto-modify content Dex relies on.

## Summary

| Enhancement | Purpose | Where it lives |
|---|---|---|
| Graph view coloring | Folder-based color groups | `.obsidian/graph.json` + `.scripts/update-obsidian-graph.cjs` |
| Bases | Database views over People / Companies / Projects | `<folder>/<Name>.base` |
| Dataview | Live queries from notes | `.obsidian/plugins/dataview/` |
| Periodic Notes | Daily note management | `.obsidian/plugins/periodic-notes/` (Daily-only) |
| Linter | Manual markdown cleanup | `.obsidian/plugins/obsidian-linter/` |
| Frontmatter schemas | YAML structure for People / Companies / Projects | `CLAUDE.md` USER_EXTENSIONS |
| Frontmatter backfill | One-pass population of existing pages | `.scripts/backfill-frontmatter.cjs` |

---

## 1. Graph View Coloring

Folder-based color groups make the graph view immediately readable: blues for strategic horizons, oranges for tasks, sepia for archives, etc.

### How to regenerate

```bash
# Preview without writing
node .scripts/update-obsidian-graph.cjs --dry-run

# Apply (writes .obsidian/graph.json, makes a daily backup)
node .scripts/update-obsidian-graph.cjs
```

After applying, reload the graph: Cmd+P → "Graph view: Open graph view".

### Palette

| Folder | Color | Rationale |
|---|---|---|
| `00-Inbox` | `#F1C40F` (yellow) | needs attention |
| `01-Quarter_Goals` | `#5B8DEF` (blue) | strategic, long horizon |
| `02-Week_Priorities` | `#00C2A8` (teal) | mid horizon |
| `03-Tasks` | `#F4845F` (orange) | hot, actionable |
| `04-Projects` | `#2ECC71` (emerald) | active work |
| `05-Areas` | `#9B59B6` (purple) | ongoing responsibilities |
| `06-Resources` | `#7F8C8D` (slate) | reference |
| `07-Archives` | `#95856B` (sepia) | historical, faded |
| `System` | `#E91E63` (pink) | config |
| `core` / `docs` / `plans` / `extensions` / `packages` | slate / indigo / gunmetal | infrastructure |

Sub-folder overrides: `05-Areas/People` (lilac), `05-Areas/Companies` (violet), `05-Areas/Career` (orchid), `00-Inbox/Meetings` (gold), `00-Inbox/Ideas` (pale yellow), `06-Resources/Meeting_Cache` (steel).

Edit the `GROUPS` array at the top of `.scripts/update-obsidian-graph.cjs` to change colors. Sub-folders are listed before parents — Obsidian applies the first matching `path:` query.

### Optional CSS defaults

`.obsidian/snippets/graph-colors.css` ships defaults for node fill, edge color, and label color in both light and dark mode. Toggle on under Settings → Appearance → CSS snippets → "graph-colors".

---

## 2. Bases

Three bases provide database-style views over Dex's structured folders. Each is filtered to its own folder and sorted by `file.mtime` descending (most recently touched first).

| Base file | Folder | What it shows |
|---|---|---|
| `05-Areas/People/People.base` | `05-Areas/People/**` | name, company, role, last_met, mtime |
| `05-Areas/Companies/Companies.base` | `05-Areas/Companies/` | name, mtime, created, source |
| `04-Projects/Projects.base` | `04-Projects/` | name, status, pillar, owner, mtime |

All three filter on `file.ext == "md"` and exclude `README` / `Untitled` to avoid noise.

### Editing a Base

Open the `.base` file in Obsidian — it renders as a table view. Sort by clicking column headers, add columns via the Properties panel, edit raw YAML by toggling "Source mode" if available. The format is plain YAML so edits can also be done in any editor.

### Adding a new column

If a property doesn't exist on most files yet, the column will show empty. Add the property to a few notes' frontmatter (matching the schemas in `CLAUDE.md`) and the column populates immediately.

---

## 3. Community Plugins

Three plugins installed, all configured to be Dex-safe.

### Dataview

Live queries over the vault. Enabled features: JS queries, inline DataviewJS, inline DQL. Use in any note:

````markdown
```dataview
TABLE WITHOUT ID file.link AS Project, status
FROM "04-Projects"
WHERE status = "active"
SORT file.mtime DESC
```
````

DataviewJS for scripted queries:

````markdown
```dataviewjs
const open = dv.pages('"03-Tasks"').file.tasks.where(t => !t.completed);
dv.list(open.text);
```
````

### Periodic Notes — Daily only

Weekly/Monthly/Quarterly disabled deliberately. Enabling them would create parallel files that compete with Dex's master-file pattern (`01-Quarter_Goals/Quarter_Goals.md`, `02-Week_Priorities/Week_Priorities.md`).

Daily notes are scoped to `00-Inbox/Daily_Plans/YYYY-MM-DD.md` to match the existing Dex convention. Use Cmd+P → "Periodic Notes: Open today's daily note".

### Linter — conservative defaults

`lintOnSave: false`. Trigger manually via Cmd+P → "Linter: Lint current file" or "Linter: Lint all files".

Enabled rules: trailing whitespace, consecutive blank lines, empty list markers, space after list markers. All YAML-mutating rules disabled. Folders excluded: `07-Archives`, `06-Resources/Meeting_Cache`, `System`, `.obsidian`, `.claude`, `.scripts`.

Add more rules cautiously — anything touching YAML or wikilinks can affect Dex automation. Test on one file first.

---

## 4. Frontmatter Schemas (Mandatory)

Defined in `CLAUDE.md` USER_EXTENSIONS. Any new page in People / Companies / Projects must follow these. Existing pages were backfilled on 2026-05-15.

### People (`05-Areas/People/**/*.md`)

```yaml
---
name: Firstname Lastname
company: <[[Company_Name]] wikilink, or string>
role: <job title>
last_met: YYYY-MM-DD
linkedin: <full URL>
---
```

### Companies (`05-Areas/Companies/*.md`)

```yaml
---
name: Company Name
domain: <e.g. mediolanum.com>
stage: <prospect | active | partner | closed>
---
```

### Projects (`04-Projects/*.md`)

```yaml
---
project: Project Name
status: <active | paused | done | archived>
pillar: <pillar id from System/pillars.yaml>
owner: Firstname Lastname
created: YYYY-MM-DD
---
```

Rules:
- Leave unknown fields empty (`key: `) rather than omitting them.
- Preserve any non-schema keys already in the file (`source`, `related`, etc.).
- When logging a new meeting, refresh `last_met` to the meeting date.
- Don't guess — empty is better than wrong for `company`, `role`, `domain`, etc.

---

## 5. Frontmatter Backfill (One-pass)

`.scripts/backfill-frontmatter.cjs` walks People / Companies / Projects and adds missing schema keys. Inference rules are intentionally conservative:

| Field | Inference source |
|---|---|
| `name` / `project` | filename (`Firstname_Lastname.md` → "Firstname Lastname") |
| `last_met` | latest `[[YYYY-MM-DD-...]]` meeting wikilink in the body |
| `company` (on person pages) | most-mentioned `[[Company_Name]]` matching an actual Companies/ file |
| `linkedin` | first `linkedin.com` URL in body |
| `status` | normalized from `**Status:** ...` marker |
| `pillar` | normalized from `**Pillar:** ...` marker |
| `domain` (on company pages) | first non-vault URL or email domain |
| `created` | inline `created:` field or file ctime |
| `owner` (on projects) | defaults to "David Orban" if absent |

### Running it again

```bash
# Always dry-run first
node .scripts/backfill-frontmatter.cjs

# Apply (creates timestamped backup at .scripts/backfill-backup-<ts>/)
node .scripts/backfill-frontmatter.cjs --apply
```

Safe to re-run — already-populated fields are not overwritten.

### Rollback

Each `--apply` run creates a full backup tree:

```bash
ls .scripts/backfill-backup-*
cp -R .scripts/backfill-backup-2026-05-15T14-28-31/* .
```

---

## What's tracked in git

`CLAUDE.md`, both scripts, the `.obsidian/` configs, and the plugin folders are committed.

Vault content under `00-Inbox/`, `04-Projects/`, `05-Areas/`, `07-Archives/` is gitignored by design (see `.gitignore`) and synced via Obsidian Sync instead. That includes the three `.base` files and the 281 backfilled markdown pages — they live locally and propagate to other devices through Sync, not git.

The backup directories (`.scripts/backfill-backup-*`) are also not committed; treat them as transient and clean up old ones when no longer needed.

---

## Quick reference: maintenance commands

```bash
# Re-color graph after palette changes
node .scripts/update-obsidian-graph.cjs

# Re-run frontmatter backfill (safe — won't overwrite filled fields)
node .scripts/backfill-frontmatter.cjs           # dry-run
node .scripts/backfill-frontmatter.cjs --apply   # write

# Clean up old backfill backups
rm -rf .scripts/backfill-backup-2026-05-15T*
```
