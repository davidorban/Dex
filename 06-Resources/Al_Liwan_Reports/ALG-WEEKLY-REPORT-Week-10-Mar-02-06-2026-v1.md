# Al Liwan Group - Weekly Report

**Week 10 | March 2-6, 2026**
**Author:** David Orban, Interim Head of Technology & Innovation
**Reporting To:** Amina Olupitan
**Reporting Date:** March 7, 2026

---

## Executive Summary

Week 10 was shaped by regional security events — Iranian missile and drone attacks on the UAE beginning over the weekend forced a government-mandated work-from-home order on Monday and disrupted operations through the first half of the week. Despite this, the IT team maintained full remote productivity, demonstrating that 100% of IT operations can be executed without physical office presence. David confirmed he plans to fly out from Abu Dhabi to Milan on Sunday March 8, working remotely for the remainder of March before Samson Giwa's start date.

The week's defining achievements were: **Intune Device Audit Report v03** produced — a comprehensive audit of device enrollment, BitLocker status, and compliance across the organization (R1); **LogicEra contract evaluation completed** — detailed clause-by-clause analysis confirming no contractual barrier to directly hiring Ankit, enabling potential transition from contractor to full-time employee (R1); **Entra ID user and service principal exports** conducted for governance baseline (R1); **Aya Mohamed offboarding fully completed** — 18 Asana tasks executed across sign-in blocking, group removal, MFA revocation, application access revocation, and mailbox conversion (R1); **MVSO security gatekeeper tasks completed** — Conditional Access baseline, BitLocker encryption baseline, M365/Entra logging, and security alerting all configured (R1); **Meeting with Amina to define new role charter** and agree on David developing the Al Liwan Labs budget (R3); **Website projects advanced** — Arabic translator replacement in process, MichaelGale.com rebuild planned with Abbas, and three Al Liwan theme implementations commissioned by Amina (R1); **AL Liwan All Hands** attended (R1); and **IB and AI session** organized for Friday with Toby, Shaheen, Axel, and the broader investment banking team (R3).

**Week at a Glance by Responsibility Area:**

| Responsibility | Charter Reference | Week 10 Focus |
|---------------|------------------|---------------|
| R1: Interim Technology Leadership | Technology governance, delivery, stabilisation | Intune Device Audit v03, LogicEra contract evaluation (Ankit hiring), Entra ID exports, Aya Mohamed offboarding completion (18 tasks), MVSO security baselines (Conditional Access, BitLocker, logging, alerting), Hibah Hadid onboarding completion, Nigeria team provisioning, IT asset management with Ankit, email domain consolidation, PitchBook SSO confirmed, CodeTwo trial expired, Ron Teams/Slack setup, daily standups, website projects (MichaelGale.com, Al Liwan themes) |
| R2: Knowledge Management | Information architecture, repositories, AI-enabled tools | RACI matrix completed and validated, service catalog shared with business lines, document formatting standardization |
| R3: AI & Innovation Enablement | AI-Native strategy, pilots, workflow adoption | New role charter development agreed with Amina, Al Liwan Labs budget to be developed, IB and AI session organized (Friday), PitchBook Claude connector deployed, MeetGeek Claude connector announced, Pingo AI evaluated for Arabic learning, Tabby MENA fintech case study |
| R4: Digital Assets Strategy | Regulated infrastructure, partnerships, use cases | IB and AI session with investment banking team |

**Critical Items Requiring Attention:**
- Regional security situation — missile/drone attacks causing psychological pressure and operational disruption; work-from-home mandated periodically
- David departing Abu Dhabi March 8 — working remotely until Samson's start date (March 23)
- LogicEra/Ankit hiring decision — contract evaluation complete, but additional verification steps recommended before proceeding
- Samson Giwa starts March 23 — pre-start meetings continuing; handover documentation being prepared
- New role charter and Al Liwan Labs budget — agreed with Amina, David to develop
- Arabic translator replacement in progress — selection expected next week
- Website: three Al Liwan theme implementations in parallel (English only, per Amina's request)

---

## Q1 KPI Progress Dashboard

### R1: Interim Technology Leadership & Stabilisation

| Q1 KPI | Target | Status | Week 10 Progress |
|--------|--------|--------|-----------------|
| Full technology baseline assessment completed | End Q1 | Advanced | Intune Device Audit Report v03 produced — comprehensive device enrollment and compliance analysis. Entra ID user and service principal exports (CSV) generated Mar 4 for governance baseline. AD properties review with Ankit — office location, manager, job title fields confirmed. |
| Core IT governance model defined | End Q1 | Near Complete | MVSO security baselines completed: Conditional Access, BitLocker, M365/Entra logging, security alerting configured. IMAP/POP disabled organization-wide. Archive mailbox and auto-expanding archive enabled. Aya Mohamed offboarding fully executed (18 tasks). Hibah Hadid onboarding completed (9 tasks). Purview confidential auto-label disabled/fixed. |

### R2: Knowledge Management & Institutional Capability

| Q1 KPI | Target | Status | Week 10 Progress |
|--------|--------|--------|-----------------|
| Knowledge management strategy approved | End Q1 | In Progress | RACI matrix completed by Cigdem and added to IT Al Liwan documentation. Service catalog shared with business lines (Hela, Izel, Axel) for validation. |
| Information architecture and documentation standards defined | End Q1 | In Progress | Document formatting standardization initiated — need for consistent templates across team identified and being addressed. Business services analysis completed at high level across all divisions. CRM consolidated services list created. |
| Core repository structure implemented | End Q1 | In Progress | IT asset management records aligned between SharePoint, AD, and Intune — Ankit consolidating device data. |

### R3: AI & Innovation Enablement

| Q1 KPI | Target | Status | Week 10 Progress |
|--------|--------|--------|-----------------|
| AI-Native strategy and roadmap approved | End Q1 | In Progress | New role charter development agreed with Amina — David to define. Al Liwan Labs budget to be developed by David. PitchBook Claude connector deployed in #innovation. MeetGeek Claude connector announced. |
| Initial pilot use cases identified | End Q1 | In Progress | IB and AI session organized for Friday with Toby O'Connor, Shaheen, Axel, Randy, Ivan, Izel. Pingo AI evaluated by Izel for Arabic language learning. Tabby MENA fintech case study shared as innovation reference. |

### R4: Digital Assets Strategy Execution

| Q1 KPI | Target | Status | Week 10 Progress |
|--------|--------|--------|-----------------|
| Digital assets strategy framework approved | End Q1 | Not Started | IB and AI session touching on digital infrastructure for investment banking |
| Priority use cases identified | End Q1 | Early Stage | IB team engagement advancing through Friday session |

---

## R1: Interim Technology Leadership & Stabilisation

*Charter mandate: Provide interim leadership of the technology function. Oversee governance, architecture, vendor selection, delivery. Assess current landscape, design sustainable operating model. Support CTO recruitment and transition.*

### Governance & Strategy

- **Regional security events and business continuity** (Mar 1-6) — Iranian missile and drone attacks on the UAE forced government-mandated work-from-home on Monday March 2. David convened a daily standup Tuesday emphasizing: all IT operations are 100% remote-capable; team shared live locations via WhatsApp group organized by Marvin; missiles intercepted by local defenses with no physical danger but significant psychological impact; Cigdem reported overnight missile sounds and shaking windows. David plans to fly out to Milan on Sunday March 8 and will work remotely for the remainder of March.
- **Daily standup** (Mar 3, with Cigdem Kemi and Ankit Choudhary) — Key topics: inventory uploads to IT hardware asset list, Intune enrollment and BitLocker status for all enrolled devices, email domain consolidation (TEG.co.A and alliwan.email persistence on some platforms), RACI matrix completion and business-line validation plan, Microsoft anti-spam ticket in progress. Safety discussion included: sharing static location pins (not live), awaiting official work-from-home guidance, confirming remote work viability.
- **Intune Device Audit Report v03** (Mar 4) — Comprehensive audit report produced (ALG-Intune-Device-Audit-Report-260304-v03.docx, 84KB) documenting device enrollment status, BitLocker compliance, and device management across the organization. Ankit confirmed BitLocker is enabled for all Intune-enrolled devices; devices not enrolled have user-managed BitLocker not under organizational control.
- **Entra ID governance exports** (Mar 4) — Exported user directory (exportUsers_2026-3-4.csv, 28KB) and service principals (exportServicePrincipals_2026-3-4.csv, 8KB) from Azure Active Directory for governance baseline analysis and reporting.
- **LogicEra contract evaluation — Ankit hiring** (Mar 5) — Detailed clause-by-clause analysis of the signed LogicEra IT Resource Augmentation Proposal V3 completed (LogicEra-Contract-Evaluation-Hiring-Ankit.docx). **Key finding: the signed agreement contains no non-solicitation, non-hire, or conversion fee clauses.** Based solely on the contract, there is no barrier to directly hiring Ankit. However, five residual risks identified: possible separate agreements, Ankit's own employment contract restrictions, visa/immigration dependency (LogicEra sponsors), relationship risk with LogicEra, and the 6-month minimum commitment (running through approximately April/May 2026). Recommendations: confirm no other agreements exist with Sherwin Loh, verify commitment period, discuss with Ankit directly, brief Legal/HR, and consider goodwill transition approach with LogicEra.
- **Mahi/David sync with LogicEra** (Mar 6) — Meeting with LogicEra representative, likely related to ongoing resource proposal and Ankit contract situation.

### Compliance & Security

- **MVSO security gatekeeper tasks completed** (Mar 6) — Four critical Minimum Viable Secure Operations tasks completed by Ankit: Configure Conditional Access baseline, Ensure disk encryption baseline (BitLocker), Configure logging baseline for M365/Entra, Configure security alerting baseline. These represent foundational security posture improvements ahead of Samson's arrival.
- **IMAP and POP disabled organization-wide** (Mar 6) — Legacy email protocols disabled for all users, reducing attack surface.
- **Archive mailbox and auto-expanding archive enabled** (Mar 6) — Mailbox archiving configured across the organization.
- **Intelligence.com blocked** (Mar 6) — Added to blocked sender list after unauthorized Entra ID consent was revoked (Mar 3).
- **PitchBook SSO confirmed working** — SSO configuration verified with PitchBook support. PitchBook user distribution list created for SSO and Claude integration.
- **ADGM.com whitelisted** — Domain added to email whitelist for regulatory communications.
- **CodeTwo Email Signatures trial expired** — Trial period ended; decision on procurement needed.

### Delivery & Operations

- **Aya Mohamed offboarding completed** (Mar 2) — Full 18-task offboarding executed by Ankit: sign-in blocked in Entra ID, all active sessions revoked, password reset, security group removal, MFA disabled, Tresorit/Asana/Slack access revoked, all other application access revoked, mailbox converted to shared, email forwarding/auto-reply configured, manager granted shared mailbox access, display name updated to include "Archive", hidden from Global Address List. Departure date confirmed with HR and data transfer requirements identified.
- **Hibah Hadid onboarding completed** (Mar 4) — Nine onboarding tasks completed: timing and readiness confirmed, hardware provisioned, account and identity setup (compliance-critical), device security and compliance configured, software and application access provided, email/calendar/collaboration tools set up, physical setup and connectivity arranged, day-1 support and handover delivered, added to Al Liwan All distribution list.
- **Nigeria team provisioning** — Ankit created onboarding templates and provided Asana, Slack, Nitro, and Tresorit access. Separate from Ron's setup.
- **Ron Teams/Slack setup** (Mar 3) — Ankit resolved Teams and Slack sign-in issues for Ron. Ron will be based in Abu Dhabi until end of April, managing his separate business. Does not require Asana/Tresorit access at this time. Will hire a permanent Abu Dhabi-based team member who will need Al Liwan accounts.
- **Dilimulati Yaermaimaiti account removed** (Mar 6) — IT orientation cancelled; account deprovisioned.
- **IT Assets and Intune Integration session** (Mar 3, with Ankit Choudhary) — Deep-dive on aligning IT asset records between SharePoint, Active Directory, and Intune. Key outcomes: SharePoint IT Hardware Asset list structure reviewed (individual entries per device); Intune syncs laptop data but peripherals require manual SharePoint entry; AD contains office location, manager, and job title fields that can be exported for location-based enrollment reporting; duplicate entries identified and flagged (e.g., Lee Pillay laptop); software cataloging approach clarified — must go beyond portal-installed apps; local admin password management via Intune LAPS reviewed (temporary passwords, rotation after use); Ankit to request fuller AD data from Nisha for cross-referencing; device location tracking capability to be verified in Intune; profile picture upload possible via AD.
- **Email domain consolidation** — Continued push to migrate remaining users from TEG.co.A and alliwan.email to alliwan.com across platforms. Slack email changes require user confirmation; Tresorit changes are self-service. Randy's separate TEG account converted to alias to free a licence.
- **Miscellaneous tickets completed** — Camille Isuan Tresorit access fixed (Mar 3), Lee Slack issue resolved (Mar 3), Stephanie finance shared mailbox assisted (Mar 2), Axel added to onlineaccounts shared mailbox (Mar 2), Hibah deleted email restored (Mar 2), emails released from quarantine and senders whitelisted (Mar 2), unwanted accounts removed (Mar 4), users added to Al Liwan All DL (Mar 4), Ron Slack verification email issue resolved (Mar 6), mail-enabled security group for alert policy created (Mar 6), domains added to whitelist (Mar 6).

### Website Delivery (Technology-Led)

- **Arabic translator replacement** — Aya Mohamed departed (accepted full-time employment elsewhere with exclusivity clause). David engaged her to vet the replacement translator's sample work. Hiring in process; new person expected next week. Identified untranslated WPML string that Aya flagged before departure.
- **MichaelGale.com rebuild** (discussed in Mar 5 Website Sync, with Abbas and Jordy) — GoDaddy hosting lost in November 2025 due to subscription lapse; files deleted after 30-day non-payment. Two source materials identified: Wayback Machine captures and a prototype David created with Manus. Claude/AI used to scaffold WordPress installation. Abbas will refine over the weekend. English-first priority; WPML and Arabic version to follow later. DNS CNAME change needed for deployment.
- **Al Liwan website — three theme implementations** (discussed in Website Sync with Abbas and Jordy) — Amina reviewed three alternative themes and requested all three be implemented (English only) for comparison before selecting. David noted the inefficiency (75% of work will be discarded) but deferred to Amina given the current stress environment. Key requirements from Amina: every click must work (no broken links or placeholders), no stock photos, no large logo placeholders. Abbas confirmed he can complete tasks over the weekend. Content must drive design, not vice versa — David instructed Abbas not to request content creation for empty design components but to adapt designs to existing content. Abbas authorized to remix strong components across themes.

### People & Coaching

- **Cigdem Kemi** — Completed RACI matrix and added to IT documentation; initiated document formatting standardization; began service catalog validation with business lines (Hela, Izel, Axel); completed business services high-level analysis and CRM consolidated services list.
- **Ankit Choudhary** — Completed Aya Mohamed offboarding (18 tasks), Hibah Hadid onboarding (9 tasks), MVSO security baselines (4 tasks), IT ticketing (15+ tasks), inventory uploads, BitLocker verification, Nigeria team provisioning, Ron setup, Intune/AD/SharePoint alignment session with David. Strong operational delivery week despite security disruption.

---

## R2: Knowledge Management & Institutional Capability

*Charter mandate: Design and implement knowledge management strategy. Ensure institutional knowledge is captured, structured, reusable. Oversee AI-assisted knowledge tools. Promote a culture of documentation and institutional learning.*

### Strategy & Architecture

- **RACI matrix completed** — Cigdem finalized the RACI matrix for IT services and added it to the IT Al Liwan documentation. Next step: validate with business lines to confirm ownership and responsibilities.
- **Service catalog shared for validation** — Shared with Hela, Izel, and Axel for review and input. Cigdem met with Hela and scheduled call with Axel to gather business-line insights as preparation for consolidated service catalog.

### Process Documentation

- **Document formatting standardization** — Cigdem identified inconsistencies between document templates created by different team members. Working on unified format, logos, and branding across IT documentation.
- **Business services analysis** — High-level analysis of business services across all divisions completed; CRM consolidated services list created for cross-divisional workflow alignment.

---

## R3: AI & Innovation Enablement

*Charter mandate: Define and lead execution of the AI-Native strategy. Oversee practical AI adoption, embedding AI-enabled workflows, tools, and governance. Act as internal sponsor for AI experimentation and pilots.*

### AI-Native Strategy Execution

- **New role charter and Al Liwan Labs budget** (meeting with Amina, Week 10) — David and Amina agreed that David will develop the new role charter defining his ongoing responsibilities, and will prepare the budget for Al Liwan Labs as the formalized innovation experimentation entity. This advances the Labs concept discussed with Marvin in Week 09 from strategic discussion to operational planning.
- **IB and AI session organized** (Mar 6, 3:00 PM) — Organized meeting with Toby O'Connor, Shaheen, Axel Zanner Entwistle, Randy, Ivan, and Izel Sequeira to explore AI applications within the investment banking division. Confirmed via Slack #ai-native-ib channel. Toby's sitrep email expressed enthusiasm and support for the hub-model approach.
- **PitchBook Claude connector deployed** — Announced in #innovation channel. Enables AI-powered access to PitchBook's private market intelligence data through Claude, supporting investment research workflows.
- **MeetGeek Claude connector announced** — Shared in #innovation as another example of the expanding Claude connector ecosystem for Al Liwan.

### Pilot Use Cases Advanced

| Pilot | Stage | Week 10 Progress |
|-------|-------|-----------------|
| Claude Enterprise Deployment | Expanding | PitchBook and MeetGeek Claude connectors deployed/announced; ecosystem growing |
| IB and AI Initiative | Organized | Friday session with full IB team (Toby, Shaheen, Axel, Randy, Ivan, Izel) |
| Al Liwan Labs | Planning | Role charter and budget development agreed with Amina |
| Arabic Language Learning (Pingo AI) | Evaluated | Axel requested Arabic learning resources in #knowledge-learning; Izel evaluated Pingo AI and shared feedback |

### AI Industry Intelligence

- **Tabby MENA fintech case study** — Shared in #innovation as reference for AI-native financial services approaches in the MENA region.
- **Pingo AI Arabic learning evaluation** — Izel Sequeira evaluated the Pingo AI Arabic language learning platform at Axel's request and shared assessment in #knowledge-learning. David coached on research methodology.

---

## R4: Digital Assets Strategy Execution

*Charter mandate: Lead development and execution of the Digital Assets strategy. Oversee translation into operating models, partnerships, technology choices, regulatory engagement. Coordinate with legal, compliance, external advisors.*

### Direct Activity

- **IB and AI session** (Mar 6) — Cross-functional meeting organized with the investment banking team to explore AI integration opportunities. This session bridges R3 (AI strategy) and R4 (digital assets infrastructure) by examining how AI tools can enhance deal sourcing, due diligence, and market intelligence workflows relevant to digital asset strategy execution.

---

## Cross-Cutting: Decisions & Approvals

| Decision | Responsibility | Status |
|----------|---------------|--------|
| David to develop new role charter | R3 | Agreed with Amina; development in progress |
| David to develop Al Liwan Labs budget | R3 | Agreed with Amina; development in progress |
| LogicEra contract — no barrier to hiring Ankit directly | R1 | Analysis complete; additional verification steps recommended |
| Three Al Liwan website themes to be implemented for Amina's review | R1 | Decided by Amina; English only, all three in parallel |
| MichaelGale.com to be rebuilt on WordPress, English first | R1 | Decided; Abbas working over weekend |
| Arabic translator replacement in process | R1 | Hiring underway; Aya to vet new candidates |
| MVSO security baselines completed | R1 | Conditional Access, BitLocker, logging, alerting all configured |
| IMAP/POP disabled organization-wide | R1 | Security hardening decision executed |
| David departing Abu Dhabi March 8, remote through March | R1 | Logistics in progress |

---

## Issues & Risks

| Risk | Responsibility | Impact | Mitigation |
|------|---------------|--------|------------|
| Regional security situation — missile/drone attacks | Cross-cutting | High — work-from-home mandated, psychological pressure, flight disruptions, business continuity stress | Full remote operations confirmed viable; location sharing organized; official guidance followed |
| David remote for remainder of March | R1 | Medium — reduced in-person oversight during transition period | All IT operations 100% remote-capable; daily standups continue; Samson Giwa starts Mar 23 |
| LogicEra contract — hiring timeline constraints | R1 | Medium — 6-month minimum commitment runs through ~Apr/May 2026; visa transition needed | Contract evaluation complete; additional verification with Sherwin Loh and Legal recommended |
| Digital assets Q1 KPI at risk | R4 | High — no dedicated strategy document started | IB and AI session provides use case exploration; needs focused writing time |
| KM strategy not yet approved | R2 | Medium — Q1 KPI requires approved strategy | RACI matrix and service catalog advancing foundation |
| Website gated on multiple dependencies | R1 | Medium — three theme implementations required, Arabic translator replacement, IPA licence still pending | English-first approach reduces critical path; Abbas working over weekend |
| CodeTwo Email Signatures trial expired | R1 | Low — email signature standardization paused | Procurement decision needed |
| MeetGeek team access issues | R3 | Low — Izel Sequeira could not accept MeetGeek invitation | Pedro resolved via backend invite; monitoring |

---

## Team & Stakeholder Engagement

- **Direct reports / function:** Ankit Choudhary (IT support — Aya offboarding 18 tasks, Hibah onboarding 9 tasks, MVSO security baselines 4 tasks, 15+ IT tickets, Intune/AD session, Nigeria team provisioning, Ron setup), Cigdem Kemi (IT Director — RACI matrix, service catalog, document formatting, business services analysis), website team (Abbas Haider, Jordy — MichaelGale.com rebuild, Al Liwan three themes).
- **Line manager:** Amina Olupitan — Meeting on new role charter and Al Liwan Labs budget; website review requesting three theme implementations; Staff Briefing (Mar 3); Al Liwan All Hands (Mar 5).
- **Peer / cross-functional:** Toby O'Connor (IB sitrep, IB and AI session organizer), Axel Zanner Entwistle (AI conversation Mar 5, Arabic learning, service catalog validation), Sherwin Loh (LogicEra contract signatory — verification needed), Amy Swartz (Weekly Sync Mar 5).
- **IT support users:** Ron (Teams/Slack setup), Camille Isuan (Tresorit fix), Lee (Slack fix), Stephanie (shared mailbox), Hibah Hadid (onboarding complete), Dilimulati Yaermaimaiti (account removed after cancelled orientation).
- **External:** Abbas Haider (website developer — MichaelGale.com and Al Liwan themes), LogicEra/Mahi (resource proposal sync), Microsoft (anti-spam ticket), PitchBook support (SSO confirmed).

---

## Operational Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| Meetings conducted | 7+ | Mon: OoO/WFH; Tue: Daily Standup, IT Assets & Intune session; Wed: Staff Briefing; Thu: Amy Sync, Daily Standup, Website Sync, AI conversation, Al Liwan All Hands; Fri: Expensify, Daily Standup, IB and AI, Mahi/LogicEra Sync |
| Asana tasks completed | 50+ | Aya offboarding (18), Hibah onboarding (9), MVSO baselines (4), IT tickets (15+), governance tasks (4+) |
| Email threads managed | 12+ | KSA IT onboarding, MeetGeek receipt (€75.40), 1Password invoice ($5.81), CodeTwo trial expired, PitchBook SSO, Smarsh/Teams recording, MeetGeek access (Izel), IB sitrep (Toby), booking confirmation, Alice catch-up cancelled, LogicEra contract |
| Key documents delivered | 5 | Intune Device Audit Report v03, LogicEra Contract Evaluation, Entra user export, Service principals export, RACI matrix |
| Projects advanced | 8+ | Intune audit, LogicEra evaluation, MVSO security, website rebuild, Al Liwan themes, IB and AI initiative, role charter, Al Liwan Labs budget |

**Time Allocation Estimate (by Responsibility):**

| Responsibility | Estimated % | Notes |
|---------------|-------------|-------|
| R1: Interim Technology Leadership | ~60% | Intune audit, LogicEra evaluation, Entra exports, MVSO baselines, Aya offboarding, Hibah onboarding, daily standups, IT assets session, website projects, operations, email consolidation |
| R2: Knowledge Management | ~10% | RACI matrix, service catalog validation, document standardization |
| R3: AI & Innovation | ~20% | Role charter agreement, Al Liwan Labs budget agreement, IB and AI session, PitchBook/MeetGeek connectors, Pingo AI evaluation |
| R4: Digital Assets | ~5% | IB and AI session (shared with R3) |
| Administrative / Cross-cutting | ~5% | Regional security management, travel logistics, WFH coordination, Expensify |

---

## Upcoming Week Priorities (Week 11)

### R1: Interim Technology Leadership
1. **David remote transition** — Complete Abu Dhabi departure; establish full remote working cadence from Milan.
2. **LogicEra / Ankit hiring next steps** — Confirm with Sherwin Loh no additional agreements exist; brief Legal/HR; discuss timeline with Ankit.
3. **Samson Giwa pre-start** — Continue pre-start meeting schedule; ensure all handover documentation current.
4. **Arabic translator onboarding** — Select and onboard replacement; Aya to vet translation quality.
5. **Website progress review** — Review Abbas's weekend work on MichaelGale.com and Al Liwan three themes.
6. **CodeTwo Email Signatures** — Decide on procurement or alternative.
7. **Intune enrollment gap analysis** — Use Entra exports and Intune audit to identify unenrolled devices.

### R2: Knowledge Management
8. **Service catalog validation** — Complete business-line validation sessions (Hela, Axel).
9. **Document template standardization** — Finalize unified templates with Cigdem.

### R3: AI & Innovation
10. **New role charter development** — Draft role charter per agreement with Amina.
11. **Al Liwan Labs budget** — Begin budget preparation for innovation entity.
12. **IB and AI follow-up** — Process outcomes from Friday session; identify next steps with Toby and team.

### R4: Digital Assets
13. **Digital assets strategy framework** — Allocate focused writing time; integrate IB and AI insights.

### Administrative
14. **Smarsh / Teams recording** — Complete review and decide on approach.
15. **MeetGeek payment confirmed** — €75.40 successfully charged (forwarded receipt to Stephanie regarding company card).

---

## Appendix A: Meeting Log

| Date | Meeting | Responsibility | Key Participants |
|------|---------|---------------|-----------------|
| Mar 1 (Sun) | SITREP Huddle | Cross-cutting | Marvin (organizer), Michael, all-hands |
| Mar 2 (Mon) | Out of Office / WFH | — | Government-mandated work from home |
| Mar 3 (Tue) | Daily Standup | R1 | David, Cigdem Kemi, Ankit Choudhary |
| Mar 3 (Tue) | IT Assets and Intune Integration | R1 | David, Ankit Choudhary |
| Mar 3 (Tue) | IT Weekly Meeting (Ankit) | R1 | David, Ankit Choudhary |
| Mar 3 (Tue) | Staff Briefing | R1 | Amina Olupitan (organizer), Slack huddle |
| Mar 4 (Wed) | Daily Standup | R1 | David, team |
| Mar 4 (Wed) | Website review with Amina | R1 | David, Amina Olupitan |
| Mar 4 (Wed) | IT Orientation (cancelled) | R1 | Dilimulati Yaermaimaiti — account removed |
| Mar 5 (Thu) | Amy/David Weekly Sync | Admin | David, Amy Swartz |
| Mar 5 (Thu) | Daily Standup | R1 | David, team |
| Mar 5 (Thu) | Website Sync | R1 | David, Abbas Haider, Jordy |
| Mar 5 (Thu) | AI Conversation | R3 | David, Sherwin Loh, Axel Zanner Entwistle |
| Mar 5 (Thu) | AL Liwan All Hands | Cross-cutting | Amina Olupitan (organizer), 56 attendees, Michael Gale |
| Mar 5 (Thu) | Quick Check-In and Setup | R1 | Pre-All Hands technical setup |
| Mar 6 (Fri) | Expensify — Hibah/David | Admin | David, Hibah Hadid |
| Mar 6 (Fri) | Daily Standup | R1 | David, team |
| Mar 6 (Fri) | IB and AI | R3/R4 | David, Toby O'Connor, Shaheen, Axel, Randy, Ivan, Izel Sequeira |
| Mar 6 (Fri) | Mahi/David Sync (LogicEra) | R1 | David, Mahi (LogicEra) |
| Week 10 | Meeting with Amina (role charter & Labs budget) | R3 | David, Amina Olupitan |

## Appendix B: Key Email Threads

| Thread | Responsibility | Status | Action Required |
|--------|---------------|--------|-----------------|
| KSA IT Onboarding — action items | R1 | In progress | Job titles, Slack approach, company domain to confirm |
| MeetGeek receipt — €75.40 | Admin | Paid | Forwarded to Stephanie re: company card |
| 1Password invoice — $5.81 | R1 | Forwarded | Expense tracking |
| CodeTwo Email Signatures trial expired | R1 | Expired | Procurement decision needed |
| PitchBook SSO working | R1 | Confirmed | Complete |
| Smarsh / Teams recording | R1 | Deferred | David still reviewing options |
| MeetGeek team access — Izel Sequeira | R3 | Resolved | Pedro resolved via backend invite |
| IB sitrep — Toby O'Connor | R3/R4 | Received | Support for hub model noted |
| David/Alice Catch Up | R1 | Cancelled | Mar 6 meeting cancelled |
| Booking confirmation | Admin | Forwarded | Travel logistics |
| Asana notifications — Ankit tasks | R1 | Ongoing | Multiple tasks added/completed |

## Appendix C: Slack Activity

| Channel | Topic | Participants | Relevance |
|---------|-------|-------------|-----------|
| #innovation | PitchBook Claude connector deployed | David Orban | R3 — AI ecosystem expansion |
| #innovation | Tabby MENA fintech case study | David Orban | R3 — Innovation reference |
| #innovation | MeetGeek Claude connector announced | David Orban | R3 — AI ecosystem expansion |
| #knowledge-learning | Axel Arabic learning request | Axel Zanner Entwistle, David, Izel | R3 — Learning & development |
| #knowledge-learning | Pingo AI evaluation | Izel Sequeira, David | R3 — AI tool evaluation |
| #ai-native-ib | IB and AI meeting confirmed 3PM Friday | Team | R3/R4 — IB AI initiative |
| #sitrep-uae-mar26 | Geopolitical discussion | Team | Cross-cutting — Regional situation |
| #news-mena | UAE exploring freezing Iranian assets (WSJ) | Team | R4 — Regulatory environment |
| #events | Event information shared | Alice Rosolen (Cristina Ventura Serra) | Cross-cutting — Events |
| #watercooler | Cigdem village photo | Cigdem Kemi | Team culture |

## Appendix D: Calendar Events

| Date | Event | Type | Key Detail |
|------|-------|------|-----------|
| Mar 1 (Sun) | SITREP Huddle | Internal | Marvin-organized, all-hands style; missile situation briefing |
| Mar 2 (Mon) | Out of Office / WFH | Personal/Gov | Government-mandated work from home due to security |
| Mar 3 (Tue) | Daily Standup | Internal | Team status — security, inventory, email consolidation |
| Mar 3 (Tue) | IT Assets and Intune Integration | Internal | Deep-dive with Ankit on asset management |
| Mar 3 (Tue) | IT Weekly Meeting | Internal | Ankit operational review |
| Mar 3 (Tue) | Staff Briefing | Internal | Amina-organized Slack huddle |
| Mar 4 (Wed) | Daily Standup | Internal | Team status |
| Mar 4 (Wed) | Website review with Amina | Internal | Three theme implementations decided |
| Mar 4 (Wed) | IT Orientation (cancelled) | Internal | Dilimulati Yaermaimaiti — account deprovisioned |
| Mar 5 (Thu) | Amy/David Weekly Sync | Internal | Administrative |
| Mar 5 (Thu) | Daily Standup | Internal | Team status |
| Mar 5 (Thu) | Website Sync | Internal | Abbas, Jordy — MichaelGale.com + Al Liwan themes |
| Mar 5 (Thu) | AI Conversation | Internal | Sherwin Loh, Axel Zanner Entwistle |
| Mar 5 (Thu) | AL Liwan All Hands | Internal | 56 attendees; Amina-organized |
| Mar 6 (Fri) | Expensify — Hibah/David | Internal | Expense processing |
| Mar 6 (Fri) | Daily Standup | Internal | Team status |
| Mar 6 (Fri) | IB and AI | Internal | Toby, Shaheen, Axel, Randy, Ivan, Izel |
| Mar 6 (Fri) | Mahi/David Sync (LogicEra) | External | Resource proposal discussion |

---

*Report structured against Role Charter dated 04/02/2026 — four responsibility areas with Q1 KPI tracking.*
*Synthesised from 5 meeting transcripts, 12+ email threads, 17 calendar events, 50+ Asana tasks, Slack activity, and week10 folder documents.*
*Week 10 | Al Liwan Group | David Orban, Interim Head of Technology & Innovation*
