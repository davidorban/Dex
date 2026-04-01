# Business Case: Darwinbox HRIS

**Date:** January 19, 2026
**Requested by:** David Orban, Head of IT / Tracey Batty-Jones, HR
**Budget Line:** Enterprise - Darwinbox HRIS (Phase 1)
**Amount:** ~$42,000-$60,000 USD (AED 154,140-220,200) Year 1 total

---

## Executive Summary

Al Liwan Group requires a lightweight HRIS system for Q1 2026 deployment that can operate until full ERP implementation (targeted Q4 2026+). Following a structured evaluation against regulatory, architectural, and operational gates, **Darwinbox** emerges as the only candidate that passes all three gates.

This is a **Phase 1 interim solution** with a clear migration path to Dynamics 365 when the organization is ready for full ERP deployment.

---

## Evaluation Summary

### Evaluation Framework Soundness Assessment

The evaluation matrix is **methodologically sound** for the following reasons:

1. **Gate-based elimination approach** - Prevents feature comparison from overriding compliance requirements
2. **Three mandatory gates** address the critical concerns:
   - Gate 1: Regulatory/Data Protection (UAE PDPL, ADGM DPR)
   - Gate 2: Hosting/Architecture (Azure alignment, UAE residency)
   - Gate 3: Operational Fit (<100 employees, <90 day deployment)
3. **Appropriate candidates evaluated** - Mix of enterprise (D365), mid-market (HiBob, Darwinbox), and SMB (BambooHR)
4. **Clear Phase 1/Phase 2 separation** - Does not pre-commit to platform decisions prematurely

### Gate Results Summary

| Vendor | Gate 1 (Regulatory) | Gate 2 (Architecture) | Gate 3 (Operational) | Status |
|--------|:-------------------:|:---------------------:|:--------------------:|--------|
| **Microsoft Dynamics 365** | ✅ Pass | ✅ Pass | ❌ Fail | Deferred (Phase 2) |
| **HiBob** | ✅ Pass | ❌ Fail (EU/US only) | ✅ Pass | Excluded |
| **Darwinbox** | ✅ Pass | ✅ Pass | ✅ Pass | **Qualified** |
| **BambooHR** | ✅ Pass | ❌ Fail (US only) | ✅ Pass | Excluded |

**Key Findings:**
- HiBob and BambooHR fail on **UAE data residency** - neither offers Middle East hosting
- Dynamics 365 fails Gate 3 - requires significant build effort, not suitable for Q1 HRIS-only deployment
- **Darwinbox is the only candidate passing all three gates**

---

## Darwinbox in Regulated UAE Organizations

### Regional Presence & Credentials

| Aspect | Details |
|--------|---------|
| **Regional Office** | Dubai International Financial Centre (DIFC) |
| **GCC Coverage** | UAE, Saudi Arabia, Bahrain, Kuwait, Oman, Qatar |
| **Regional Customers** | Lulu Group, Aramex, Mobily Infotech |
| **Global Customers** | Nivea, Starbucks, Sephora, Zara, AXA |
| **Scale** | 1.5M+ employees across 650+ enterprises globally |
| **Unicorn Status** | Achieved in 2023 with $72M funding round |
| **Regional Partner** | PwC Middle East (preferred implementation partner) |

### Security & Compliance Certifications

| Certification | Status | Relevance to Al Liwan |
|---------------|--------|----------------------|
| **ISO 27001** | ✅ Certified | Information security management |
| **SOC 2 Type II** | ✅ Certified | Security controls attestation |
| **ISO 27701** | ✅ Certified | Privacy information management |
| **GDPR** | ✅ Compliant | Data protection standard |
| **UAE Labor Law** | ✅ Supported | GCC-specific compliance |

### UAE-Specific Features

- 100% mobile self-service (pay slips, HR letters)
- Arabic mobile app (launching for MENA)
- UAE/GCC labor law compliance built-in
- Middle East data hosting options
- WPS (Wage Protection System) support

---

## Cost Analysis

### Licensing Costs (56 baseline employees, scaling to 75)

**Pricing Model:** Per-employee-per-month (PEPM), subscription-based

| Source | PEPM Rate | Annual (56 users) | Annual (75 users) |
|--------|-----------|-------------------|-------------------|
| Low estimate | $5/user/month | $3,360 | $4,500 |
| Mid estimate | $15/user/month | $10,080 | $13,500 |
| High estimate | $25/user/month | $16,800 | $22,500 |

**Recommended Budget:** $12,000-$18,000/year licensing (mid-range estimate)

*Note: Darwinbox offers tiered pricing with discounts at higher employee counts. Actual quote required.*

### Implementation Costs

| Component | Low | High | Notes |
|-----------|-----|------|-------|
| Base Implementation | $10,000 | $25,000 | Configuration, data migration |
| Customization | $2,000 | $8,000 | UAE-specific workflows |
| Integration (Entra ID SSO) | $2,000 | $5,000 | Microsoft identity integration |
| Training | $1,000 | $3,000 | Admin and end-user training |
| **Total Implementation** | **$15,000** | **$41,000** | One-time Year 1 |

### Year 1 Total Cost Model

| Scenario | Licensing | Implementation | Total (USD) | Total (AED) |
|----------|-----------|----------------|-------------|-------------|
| **Conservative** | $10,000 | $15,000 | $25,000 | 91,750 |
| **Baseline** | $15,000 | $27,000 | $42,000 | 154,140 |
| **Growth** | $18,000 | $42,000 | $60,000 | 220,200 |

### Ongoing Annual Cost (Year 2+)

| Scenario | Annual Licensing | Annual Support | Total (USD) |
|----------|-----------------|----------------|-------------|
| Conservative | $10,000 | $2,000 | $12,000 |
| Baseline | $15,000 | $3,000 | $18,000 |
| Growth | $22,500 | $4,500 | $27,000 |

---

## Implementation Timeline

**Target: Production by end of Q1 2026**

| Phase | Duration | Activities |
|-------|----------|------------|
| **Week 1-2** | 2 weeks | Contract, environment setup, data mapping |
| **Week 3-6** | 4 weeks | Configuration, data migration, SSO integration |
| **Week 7-8** | 2 weeks | UAT, training, go-live preparation |
| **Week 9-10** | 2 weeks | Go-live, hypercare support |

**Total: ~10 weeks** (within 90-day Gate 3 requirement)

---

## Phase Strategy Alignment

### Phase 1 (Q1 2026) - Darwinbox
- ✅ Lightweight, compliant HRIS
- ✅ Fast deployment (<90 days)
- ✅ Minimal operational friction
- ✅ Interim HR team can manage
- ✅ Clean data model for future migration

### Phase 2 (Q4 2026+) - Dynamics 365 Evaluation
- Unified ERP/HCM platform consideration
- Triggered when:
  - Finance transitions off Xero
  - Internal product ownership resourced
  - ERP scope formally approved
  - Employee count exceeds 150+

### Data Portability

Darwinbox provides:
- Secure, documented APIs for data extraction
- Standard data export formats
- No vendor lock-in architecture
- Clean migration path to D365 HCM module

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Implementation delay | Medium | Medium | PwC partnership provides experienced local resources |
| Integration complexity | Low | Medium | Native Entra ID SSO support; documented APIs |
| Vendor lock-in | Low | Low | Clean data export; API-first architecture |
| Feature gaps vs D365 | Medium | Low | Phase 1 focuses on core HR; advanced features in Phase 2 |
| Regional support quality | Low | Medium | DIFC office; PwC local partner |

---

## Recommendation

**Approve Darwinbox HRIS for Phase 1 deployment** with the following budget allocation:

| Scenario | Year 1 (USD) | Year 1 (AED) | Budget Line |
|----------|--------------|--------------|-------------|
| Conservative | $0 | 0 | Not included |
| **Baseline** | $42,000 | 154,140 | Enterprise - Darwinbox HRIS |
| Growth | $60,000 | 220,200 | Enterprise - Darwinbox HRIS |

### Next Steps

1. Request formal quote from Darwinbox for 56-75 employees
2. Engage PwC Middle East for implementation scoping
3. Schedule technical demo with IT team
4. Confirm Entra ID SSO integration requirements
5. Target contract signature by end of January 2026

---

## Sources

- [Darwinbox Middle East Expansion](https://gulfbusiness.com/darwinbox-accelerates-mena-expansion-after-leaping-to-unicorn-status/)
- [PwC Middle East Darwinbox Alliance](https://www.pwc.com/m1/en/media-centre/2024/pwc-alliance-human-capital-management-platform-darwinbox.html)
- [Darwinbox Security & Architecture](https://darwinbox.com/en-us/company/security-and-architecture)
- [Darwinbox Pricing Guide](https://www.itqlick.com/darwinbox/pricing)
- [Gartner Peer Insights - Darwinbox](https://www.gartner.com/reviews/market/cloud-hcm-suites-for-1000-employees/vendor/darwinbox/product/darwinbox)
- Internal: ALG-HRIS-Eval-260116.docx, ALG-Eval-Matrix-HRIS-260116.docx
