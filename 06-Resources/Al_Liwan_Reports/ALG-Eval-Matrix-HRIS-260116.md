# HRIS Evaluation Matrix

**Al Liwan Group | Q1 2026**

## Purpose

To evaluate HRIS candidates against **regulatory, architectural, and operational constraints** specific to Al Liwan, before feature comparison or vendor branding considerations.

This matrix is designed to:

* enforce early elimination of non-viable options,
* align HR, IT, Security, and Corporate Strategy,
* support a Phase 1 implementation with a clear Phase 2 migration path.

---

## Evaluation Model

The evaluation proceeds in **three mandatory gates**, followed by a **comparative scorecard**.

* **Gate failure = exclusion or deferral**, regardless of vendor reputation.
* Passing all gates qualifies a system for shortlisting.

---

## Gate 1: Regulatory and Data Protection Viability (Pass / Fail)

**Objective:** Ensure compliance with UAE PDPL and ADGM DPR obligations.

| Criterion                           | Requirement                                      | Pass / Fail | Notes |
| ----------------------------------- | ------------------------------------------------ | ----------- | ----- |
| Data Controller / Processor Clarity | Vendor contractually acts as Data Processor      |             |       |
| DPA Availability                    | GDPR-grade Data Processing Agreement available   |             |       |
| Sub-processor Transparency          | Full sub-processor list disclosed and governed   |             |       |
| Cross-Border Transfer Mechanism     | Lawful transfer basis clearly documented         |             |       |
| Data Subject Rights Support         | Access, correction, deletion workflows supported |             |       |
| Breach Notification SLA             | Explicit breach notification timelines           |             |       |
| Audit Rights                        | Right to audit or receive independent assurance  |             |       |

**Gate 1 Outcome:**

* Pass ☐
* Fail ☐
* Deferred ☐

---

## Gate 2: Hosting, Identity, and Architecture Fit (Pass / Fail)

**Objective:** Validate technical and architectural compatibility with Al Liwan’s Microsoft-centric environment and data residency expectations.

| Criterion              | Requirement                                                | Pass / Fail | Notes |
| ---------------------- | ---------------------------------------------------------- | ----------- | ----- |
| Hosting Model          | SaaS acceptable only if residency is contractually defined |             |       |
| UAE Data Residency     | UAE-hosted or legally defensible transfer model            |             |       |
| Azure Dependency       | Runs on Azure or interoperates cleanly with Azure          |             |       |
| Tenant Control         | Clear separation between vendor tenant and Al Liwan tenant |             |       |
| Identity Integration   | Native Entra ID (Azure AD) SSO                             |             |       |
| MFA and RBAC           | Fine-grained role-based access controls                    |             |       |
| API Availability       | Secure, documented APIs for integrations                   |             |       |
| Logging and Monitoring | Exportable audit logs                                      |             |       |

**Gate 2 Outcome:**

* Pass ☐
* Fail ☐
* Deferred ☐

---

## Gate 3: Operational and Organizational Fit (Pass / Fail)

**Objective:** Ensure the system is appropriate for a sub-100-employee organization with limited internal HR and IT bandwidth.

| Criterion                | Requirement                               | Pass / Fail | Notes |
| ------------------------ | ----------------------------------------- | ----------- | ----- |
| Minimum Viable Scale     | Designed for <100–250 employees           |             |       |
| Implementation Time      | <90 days to production                    |             |       |
| Configuration Complexity | No heavy custom development required      |             |       |
| HR Admin Load            | Manageable by interim HR function         |             |       |
| Vendor Responsiveness    | Realistic access to demos and support     |             |       |
| Cost Structure           | Predictable, non-enterprise pricing       |             |       |
| Exit Path                | Data export and future migration feasible |             |       |

**Gate 3 Outcome:**

* Pass ☐
* Fail ☐
* Deferred ☐

---

## Shortlist Qualification

Only systems that **pass all three gates** proceed to scoring.

---

## Comparative Scorecard (Qualified Candidates Only)

| Dimension                | Weight | Vendor A | Vendor B | Vendor C |
| ------------------------ | ------ | -------- | -------- | -------- |
| Core HR Functionality    | 20%    |          |          |          |
| Security Maturity        | 20%    |          |          |          |
| Microsoft Ecosystem Fit  | 15%    |          |          |          |
| UX and Adoption          | 15%    |          |          |          |
| Reporting and Analytics  | 10%    |          |          |          |
| Vendor Viability         | 10%    |          |          |          |
| Cost vs Value            | 10%    |          |          |          |
| **Total Weighted Score** | 100%   |          |          |          |

---

## Phase Strategy Alignment

**Phase 1 (2026):**

* Lightweight, compliant HRIS
* Fast deployment
* Minimal operational friction

**Phase 2 (Future):**

* Optional migration to enterprise HCM
* Data portability preserved
* No regulatory rework required

---

## Decision Record

* **Recommended System:**
* **Decision Rationale:**
* **Known Tradeoffs:**
* **Next Review Trigger:** (e.g. 300+ employees, multi-country payroll, etc.)