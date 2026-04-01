# Dex — Local Setup (David Orban)

AI Chief of Staff kit. 25+ skills for daily planning, relationship tracking, meeting prep, project health, and commitment management.

## Installation
- **Installed:** 2026-03-20
- **Repo:** `~/Dev/Dex`
- **Method:** `git clone https://github.com/davekilleen/Dex.git` + `PATH="/opt/homebrew/bin:$PATH" bash install.sh`
- **Node:** v23.9.0 ✓
- **Python:** 3.13.11 (brew) ✓ — symlinked via `ln -sf /opt/homebrew/bin/python3.13 /opt/homebrew/bin/python3`
- **Work MCP Python deps:** Failed to install (non-critical — task sync won't work, everything else does)

## First-Time Setup

Run `/setup` inside Claude Code from the `~/Dev/Dex` directory. It will ask about your role, calendar, and preferences.

```bash
# Open Claude Code in the Dex directory
claude ~/Dev/Dex
# Then run: /setup
```

## Daily Use

```
/daily-plan       — Morning planning based on calendar + tasks
/meeting-prep     — Context brief before a call
/review           — End-of-day review
/task             — Add a task
```

## API Key (for background processing only)

99% of features work through Claude Code without any API key. The key is only needed for background meeting processing when Claude Code is closed.

To enable: copy `env.example` to `.env` and add one key:

```bash
cp env.example .env
# Edit .env — add ANTHROPIC_API_KEY from 1Password
# Item: search 1Password for Anthropic key
```

## Updating

```bash
cd ~/Dev/Dex
git pull
PATH="/opt/homebrew/bin:$PATH" bash install.sh
```

## Notes
- Dex renames `origin` → `upstream` during install to avoid Claude Desktop confusion
- Work MCP (Python task sync) requires `mcp` and `pyyaml` pip packages — install with:
  ```bash
  /opt/homebrew/bin/pip3.13 install mcp pyyaml
  ```
  Then re-run `install.sh`
