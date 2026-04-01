#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

// --- Configuration ---
const VAULT_ROOT = path.resolve(__dirname, '..');
const PEOPLE_DIRS = [
  path.join(VAULT_ROOT, '05-Areas/People/Internal'),
  path.join(VAULT_ROOT, '05-Areas/People/External'),
];
const TODAY_FILES = [
  '03-Tasks/Tasks.md',
  '02-Week_Priorities/Week_Priorities.md',
];

// --- Registry Builder ---

function buildRegistry() {
  const registry = {
    // fullName → { file: 'Firstname_Lastname', display: 'Firstname Lastname' }
    byFullName: new Map(),
    // firstName → [{ file, display, fullName }]  (only safe if unambiguous)
    byFirstName: new Map(),
    // All known first names (for unknown-fullname detection)
    allFirstNames: new Set(),
  };

  for (const dir of PEOPLE_DIRS) {
    if (!fs.existsSync(dir)) continue;
    const files = fs.readdirSync(dir).filter(f => f.endsWith('.md') && f !== 'README.md');

    for (const file of files) {
      const stem = file.replace('.md', '');
      // Convert filename to display name: Firstname_Lastname → Firstname Lastname
      // Handle special cases: d'Ambrosa, O'Connor, etc.
      const display = stem
        .replace(/_/g, ' ')
        .replace(/\bd([A-Z])/g, "d'$1")  // dAmbrosa → d'Ambrosa
        .replace(/\bO([A-Z])/g, "O'$1"); // OConnor → O'Connor

      const parts = display.split(' ');
      const firstName = parts[0];
      const fullName = display;

      registry.byFullName.set(fullName.toLowerCase(), { file: stem, display: fullName });

      // Also register common variants
      // "Tracey Batty Jones" should match "Tracey Batty-Jones" etc.
      if (stem.includes('_Batty_Jones')) {
        registry.byFullName.set('tracey batty-jones', { file: stem, display: fullName });
      }

      registry.allFirstNames.add(firstName.toLowerCase());

      // Track first names for ambiguity detection
      if (!registry.byFirstName.has(firstName.toLowerCase())) {
        registry.byFirstName.set(firstName.toLowerCase(), []);
      }
      registry.byFirstName.get(firstName.toLowerCase()).push({
        file: stem,
        display: fullName,
        fullName: fullName.toLowerCase(),
      });
    }
  }

  return registry;
}

// --- Content Processor ---

function autoLinkContent(content, registry) {
  const lines = content.split('\n');
  const result = [];
  let inFrontmatter = false;
  let frontmatterCount = 0;
  let inCodeBlock = false;

  // Collect all "Firstname Lastname" patterns in the document that are NOT in our registry
  // These represent unknown people whose first names should not be auto-linked
  const unknownFullNames = new Set();
  const fullNamePattern = /\b([A-Z][a-z]+)\s+([A-Z][a-z]+(?:[-'][A-Z][a-z]+)*)\b/g;
  let match;
  while ((match = fullNamePattern.exec(content)) !== null) {
    const candidate = `${match[1]} ${match[2]}`.toLowerCase();
    if (!registry.byFullName.has(candidate)) {
      // Unknown full name — mark its first name as unsafe for standalone linking
      unknownFullNames.add(match[1].toLowerCase());
    }
  }

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // Track frontmatter (---) blocks
    if (line.trim() === '---') {
      frontmatterCount++;
      if (frontmatterCount === 1) inFrontmatter = true;
      if (frontmatterCount === 2) inFrontmatter = false;
      result.push(line);
      continue;
    }
    if (inFrontmatter) {
      result.push(line);
      continue;
    }

    // Track code blocks
    if (line.trim().startsWith('```')) {
      inCodeBlock = !inCodeBlock;
      result.push(line);
      continue;
    }
    if (inCodeBlock) {
      result.push(line);
      continue;
    }

    // Skip lines that are already WikiLinks or inside table headers
    // Don't process the person page's own title (# Firstname Lastname)
    if (i === 0 && line.startsWith('# ')) {
      result.push(line);
      continue;
    }

    // Process full names first (longest match wins)
    // Sort by length descending so "Eva Marie Muller Stuler" matches before "Eva Marie"
    const sortedNames = [...registry.byFullName.entries()]
      .sort((a, b) => b[0].length - a[0].length);

    for (const [nameLower, entry] of sortedNames) {
      // Build a case-insensitive regex for the name
      // Escape special regex chars in the name
      const escaped = entry.display.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      // Match the name but NOT if already inside [[ ]] or preceded by [[ or followed by ]]
      const nameRegex = new RegExp(
        `(?<!\\[\\[)(?<!\\|)\\b(${escaped})\\b(?!\\]\\])(?!\\|)`,
        'gi'
      );

      line = line.replace(nameRegex, (matched) => {
        return `[[${entry.file}|${matched}]]`;
      });
    }

    // Process unambiguous first names (only if exactly one person has that first name)
    for (const [firstNameLower, entries] of registry.byFirstName.entries()) {
      // Skip if ambiguous (multiple people share first name)
      if (entries.length !== 1) continue;
      // Skip if this first name appeared as part of an unknown full name
      if (unknownFullNames.has(firstNameLower)) continue;
      // Skip very short names (3 chars or less) — too many false positives
      if (firstNameLower.length <= 3) continue;
      // Skip common English words that happen to be names
      const skipWords = new Set(['alice', 'jerry', 'randy', 'luke', 'maria', 'paula', 'nisha', 'grace', 'mark']);
      // Actually, we want to link these — they're real people. Only skip truly generic words.
      const genericWords = new Set(['will', 'bill', 'mark', 'dawn', 'hope', 'joy', 'may']);
      if (genericWords.has(firstNameLower)) continue;

      const entry = entries[0];
      const escaped = entry.display.split(' ')[0].replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

      // Only match standalone first name (not already part of a WikiLink)
      const firstNameRegex = new RegExp(
        `(?<!\\[\\[)(?<!\\[\\[[^\\]]*?)(?<!\\|)\\b(${escaped})\\b(?!\\]\\])(?![^\\[]*?\\]\\])(?!\\|)`,
        'gi'
      );

      line = line.replace(firstNameRegex, (matched) => {
        // Don't link if this occurrence is already inside a WikiLink
        // (the negative lookbehind may not catch all cases with nested content)
        return `[[${entry.file}|${matched}]]`;
      });
    }

    // Clean up any double-linked names (WikiLink inside WikiLink)
    line = line.replace(/\[\[([^\]]+)\|\[\[([^\]]+)\|([^\]]+)\]\]\]\]/g, '[[$2|$3]]');

    result.push(line);
  }

  return result.join('\n');
}

// --- File Processor ---

function processFile(filePath, registry, dryRun = false) {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }

  const original = fs.readFileSync(filePath, 'utf-8');
  const linked = autoLinkContent(original, registry);

  if (original === linked) {
    console.log(`  [skip] ${path.relative(VAULT_ROOT, filePath)} (no changes)`);
    return false;
  }

  const changes = countChanges(original, linked);

  if (dryRun) {
    console.log(`  [dry-run] ${path.relative(VAULT_ROOT, filePath)} (${changes} links would be added)`);
    return false;
  }

  fs.writeFileSync(filePath, linked, 'utf-8');
  console.log(`  [linked] ${path.relative(VAULT_ROOT, filePath)} (${changes} links added)`);
  return true;
}

function countChanges(original, linked) {
  const origLinks = (original.match(/\[\[/g) || []).length;
  const newLinks = (linked.match(/\[\[/g) || []).length;
  return newLinks - origLinks;
}

// --- Today's Files ---

function findTodayFiles() {
  const today = new Date().toISOString().slice(0, 10); // YYYY-MM-DD
  const files = [];

  // Fixed files
  for (const rel of TODAY_FILES) {
    const full = path.join(VAULT_ROOT, rel);
    if (fs.existsSync(full)) files.push(full);
  }

  // Today's daily plan if it exists
  const dailyPlanGlob = path.join(VAULT_ROOT, '00-Inbox', `${today}*.md`);
  // Use simple readdir approach
  const inboxDir = path.join(VAULT_ROOT, '00-Inbox');
  if (fs.existsSync(inboxDir)) {
    for (const f of fs.readdirSync(inboxDir)) {
      if (f.startsWith(today) && f.endsWith('.md')) {
        files.push(path.join(inboxDir, f));
      }
    }
  }

  // Today's meetings
  const meetingsDir = path.join(VAULT_ROOT, '00-Inbox/Meetings');
  if (fs.existsSync(meetingsDir)) {
    for (const f of fs.readdirSync(meetingsDir)) {
      if (f.startsWith(today) && f.endsWith('.md')) {
        files.push(path.join(meetingsDir, f));
      }
    }
  }

  return files;
}

// --- CLI ---

function main() {
  const args = process.argv.slice(2);

  if (args.includes('--help') || args.includes('-h')) {
    console.log(`
auto-link-people.cjs — Convert people names to [[WikiLinks]] in markdown files

Usage:
  node auto-link-people.cjs <file-path>        Link people in a specific file
  node auto-link-people.cjs --today             Link people in today's key files
  node auto-link-people.cjs --dry-run <file>    Preview changes without writing
  node auto-link-people.cjs --stats             Show registry stats

Scans 05-Areas/People/ for person pages, builds a name registry,
and replaces mentions with [[Firstname_Lastname|Name]] WikiLinks.

Skips: frontmatter, code blocks, existing WikiLinks, ambiguous first names,
and first names that appear as part of unknown full names.
`);
    process.exit(0);
  }

  const registry = buildRegistry();
  const dryRun = args.includes('--dry-run');
  const filteredArgs = args.filter(a => !a.startsWith('--'));

  if (args.includes('--stats')) {
    console.log(`People registry:`);
    console.log(`  Full names: ${registry.byFullName.size}`);
    console.log(`  Unique first names: ${registry.byFirstName.size}`);
    const unambiguous = [...registry.byFirstName.values()].filter(v => v.length === 1).length;
    console.log(`  Unambiguous first names: ${unambiguous} (safe for standalone linking)`);
    const ambiguous = [...registry.byFirstName.entries()]
      .filter(([, v]) => v.length > 1)
      .map(([k, v]) => `${k} (${v.length}: ${v.map(e => e.display).join(', ')})`);
    if (ambiguous.length > 0) {
      console.log(`  Ambiguous first names: ${ambiguous.join('; ')}`);
    }
    process.exit(0);
  }

  if (args.includes('--today')) {
    const files = findTodayFiles();
    if (files.length === 0) {
      console.log('No files found for today.');
      process.exit(0);
    }
    console.log(`Processing ${files.length} file(s) for today:`);
    let changed = 0;
    for (const f of files) {
      if (processFile(f, registry, dryRun)) changed++;
    }
    console.log(`Done. ${changed} file(s) updated.`);
    process.exit(0);
  }

  if (filteredArgs.length === 0) {
    console.error('Usage: node auto-link-people.cjs <file-path> | --today | --stats');
    process.exit(1);
  }

  // Process specific file(s)
  let changed = 0;
  for (const arg of filteredArgs) {
    const filePath = path.resolve(arg);
    if (processFile(filePath, registry, dryRun)) changed++;
  }
  if (filteredArgs.length > 1) {
    console.log(`Done. ${changed}/${filteredArgs.length} file(s) updated.`);
  }
}

// --- Module Export ---
module.exports = { autoLinkContent, buildRegistry };

// Run CLI if invoked directly
if (require.main === module) {
  main();
}
