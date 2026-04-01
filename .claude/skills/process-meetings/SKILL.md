---
name: process-meetings
description: Process meetings from MeetGeek (or Granola) to update person pages, extract tasks, and organize meeting notes
model_hint: balanced
context: fork
hooks:
  PostToolUse:
    - matcher: Write
      type: command
      command: "node .claude/hooks/post-meeting-person-update.cjs"
  Stop:
    - type: command
      command: "node .claude/hooks/meeting-summary-generator.cjs"
---

# Process Meetings

Process meetings from MeetGeek (primary) or Granola into Dex. Updates person pages, extracts tasks, and organizes meeting notes.

## How It Works

**MeetGeek (primary):** Uses MeetGeek MCP tools to fetch meetings directly. No background sync needed — data is live.

**Granola (fallback):** If configured, reads from background-synced files in `00-Inbox/Meetings/`.

The meeting source is configured in `System/user-profile.yaml` → `meeting_processing.source`.

## Arguments

- No arguments: Process all unprocessed meetings from the last 7 days
- `today`: Only process today's meetings
- `"search term"`: Find meetings by title/attendee
- `--people-only`: Only update person/company pages (skip tasks)
- `--no-todos`: Create notes but don't extract tasks
- `--source meetgeek|granola`: Override configured source for this run

---

## Process

### Step 1: Determine Meeting Source

Read `System/user-profile.yaml` → `meeting_processing.source`.

- **If `meetgeek`:** Use MeetGeek MCP tools (Step 2a)
- **If `granola`:** Use Granola background sync files (Step 2b)

### Step 2a: Fetch Meetings from MeetGeek

Use MeetGeek MCP tools to fetch recent meetings:

1. **List meetings:** Call `meetgeek:meetings` to get meetings from the last 7 days (or today if `today` arg)
2. **For each meeting**, fetch details:
   - Call `meetgeek:meetingDetails` for metadata (title, date, participants, duration)
   - Call `meetgeek:summary` for AI-generated summary and action items
   - Call `meetgeek:transcript` for full transcript (store for reference)
   - Call `meetgeek:highlights` for key moments

3. **Check processing state:** Read `.scripts/meeting-intel/processed-meetings.json` (create if missing)
   - Skip meetings whose ID is already in the processed list
   - Track by MeetGeek meeting ID

4. **Save meeting note** to `00-Inbox/Meetings/YYYY-MM-DD - {Meeting Title}.md`:
   ```markdown
   ---
   date: {YYYY-MM-DD}
   source: meetgeek
   meetgeek_id: {meeting_id}
   participants: [{names}]
   duration: {minutes}
   ---

   # {Meeting Title}

   **Date:** {date} | **Duration:** {duration} min

   ## Participants
   {list of participants with roles if available}

   ## Summary
   {AI summary from MeetGeek}

   ## Key Highlights
   {highlights from MeetGeek}

   ## Action Items

   ### For Me
   {action items assigned to user}

   ### For Others
   {action items for other participants}

   ## Transcript
   <details>
   <summary>Full transcript</summary>

   {transcript with speaker labels}

   </details>
   ```

5. **Update processed state** with meeting ID and timestamp.

Report findings:
> "Found X meetings from MeetGeek (last 7 days). Y are new, Z already processed."

### Step 2b: Fetch Meetings from Granola (Fallback)

Check if background sync is set up:

```bash
ls .scripts/meeting-intel/processed-meetings.json
```

**If state file exists:** Read synced meeting files from `00-Inbox/Meetings/`.

**If not:** Guide user to set up Granola background sync:
> "Background meeting sync isn't set up. Run `/process-meetings --setup` or switch to MeetGeek with `/process-meetings --source meetgeek`."

For each meeting file:
1. Read frontmatter to get `granola_id`, `participants`, `company`, `date`
2. Check if person/company pages need updating
3. Check if tasks need extracting

### Step 3: Update Person Pages

For each participant in meetings:

1. **Load user profile** for email domain:
   ```
   Read System/user-profile.yaml → get email_domain
   ```

2. **Classify as Internal/External:**
   - If participant email domain matches user's domain → Internal
   - Otherwise → External

3. **Check if person page exists:**
   - Internal: `05-Areas/People/Internal/{Name}.md`
   - External: `05-Areas/People/External/{Name}.md`

4. **If page doesn't exist, create it:**
   ```markdown
   # {Name}

   ## Overview

   | Field | Value |
   |-------|-------|
   | **Company** | {company from meeting} |
   | **Email** | {if available} |
   | **First Met** | {meeting date} |

   ## Recent Interactions

   - [{Meeting Title}](00-Inbox/Meetings/{date}/{slug}.md) — {date}

   ## Notes

   *Auto-created from meeting on {date}*
   ```

5. **If page exists, add meeting to Recent Interactions:**
   - Read existing page
   - Add new meeting link under "## Recent Interactions"
   - Keep max 20 entries (remove oldest if needed)
   - Update "Last Interaction" in frontmatter

### Step 4: Update Company Pages

For each unique external company domain:

1. **Check if company page exists:** `05-Areas/Companies/{Company}.md`

2. **If doesn't exist, create it:**
   ```markdown
   # {Company Name}

   ## Overview

   | Field | Value |
   |-------|-------|
   | **Website** | {domain} |
   | **Stage** | Unknown |
   | **First Contact** | {date} |

   ## Key Contacts

   - [[05-Areas/People/External/{Person}|{Person}]]

   ## Meeting History

   - [{Meeting Title}](00-Inbox/Meetings/{date}/{slug}.md) — {date}

   ## Notes

   *Auto-created from meeting on {date}*
   ```

3. **If exists, update:**
   - Add any new contacts to "Key Contacts"
   - Add meeting to "Meeting History"

### Step 4.5: Semantic Enrichment (if QMD available)

**Check if semantic search is available** by looking for `qmd` in PATH.

If available, enhance meeting processing with meaning-based intelligence:

1. **Detect implicit commitments:** For each meeting's discussion notes, search semantically:
   ```
   qmd query "we should circle back on..." --limit 3
   qmd query "let me think about..." --limit 3
   ```
   Catch soft commitments that regex action-item extraction misses.
   - Examples: "we should probably revisit the pricing model" → implicit action item
   - "I need to noodle on the migration approach" → implicit commitment
   - "Let's reconnect after the board meeting" → implicit follow-up

2. **Link meetings to projects:** For the meeting topic, search:
   ```
   qmd query "meeting topic/title" --limit 3
   ```
   against `04-Projects/` to auto-link the meeting to relevant projects that keyword matching would miss.

3. **Enrich person context:** For each new person encountered, search:
   ```
   qmd query "person name + company" --limit 3
   ```
   Find if they've been mentioned in other meetings/notes, even if they weren't a direct participant.

**Integration:**
- Add implicit commitments to the action items list with a note: "*(detected — not explicitly stated)*"
- Add project links to meeting frontmatter
- Merge person context into newly-created person pages
- If QMD unavailable, skip silently — regex extraction still works

### Step 5: Extract Tasks (unless --no-todos or --people-only)

For each meeting with unextracted tasks:

1. **Find action items** in the "## Action Items > ### For Me" section
2. **For each unchecked item** (`- [ ]`):
   - Extract task description
   - Get task ID (format: `^task-YYYYMMDD-XXX`)
   - Read pillar from meeting frontmatter

3. **Create task** using Work MCP:
   ```
   create_task(
     title: "Task description",
     priority: "P2",  // default, P1 if "urgent" mentioned
     pillar: "{from meeting}",
     people: ["{participants}"],
     source: "meeting:{meeting-path}"
   )
   ```

4. **Mark as extracted** by adding comment to meeting note:
   ```markdown
   <!-- tasks-extracted: 2026-02-03T10:30:00Z -->
   ```

### Step 6: Summary Report

```
## Meeting Processing Complete ✅

**Synced meetings found:** X (last 7 days)
**Background sync status:** Running (last sync: 10 min ago)

### Updates Made

**Person pages:**
- Created: 3 new (Alice Chen, Bob Smith, Carol Wang)
- Updated: 5 existing

**Company pages:**
- Created: 1 new (Acme Corp)
- Updated: 2 existing

**Tasks extracted:** 7 items added to 03-Tasks/Tasks.md

### Recent Meetings

| Date | Meeting | Company | Participants |
|------|---------|---------|--------------|
| Feb 3 | Product Review | Acme | Alice, Bob |
| Feb 2 | Strategy Call | BigCo | Carol |

---
*Background sync runs every 30 min. Check status: `.scripts/meeting-intel/install-automation.sh --status`*
```

## Error Handling

**If no meetings found:**
> "No meetings synced in the last 7 days. Make sure:
> 1. Granola is running during your meetings
> 2. Background sync is set up (run `/process-meetings --setup`)
> 3. Check logs: `.scripts/logs/meeting-intel.stdout.log`"

**If background sync isn't running:**
> "Background sync appears to be stopped. To restart:
> ```bash
> cd .scripts/meeting-intel && ./install-automation.sh
> ```"

## Examples

```
/process-meetings
```
> "Found 8 synced meetings. Updating 12 person pages, extracting 5 tasks..."

```
/process-meetings today
```
> "Found 2 meetings from today. Processing..."

```
/process-meetings --setup
```
> "Installing background automation..." [runs install script]

```
/process-meetings --people-only
```
> "Updating person and company pages only (skipping task extraction)..."

---

## Track Usage (Silent)

Update `System/usage_log.md` to mark meeting processing as used.

**Analytics (Silent):**

Call `track_event` with event_name `meetings_processed` and properties:
- `meetings_count`: number of meetings processed
- `people_created`: number of new person pages created
- `todos_extracted`: number of tasks extracted

This only fires if the user has opted into analytics. No action needed if it returns "analytics_disabled".
