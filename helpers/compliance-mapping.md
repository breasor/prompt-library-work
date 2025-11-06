---
layout: page
id: compliance-mapping
title: "Compliance Mapping Framework"
role: "Governance & Standards Alignment"
category: "Regulatory & Security Frameworks"
complexity: "High"
output-format: "Markdown"
description: >
  Maps InfoSec controls and prompt outputs to major compliance frameworks relevant to healthcare and SaaS environments.
tags:
 - compliance
 - NIST
 - CIS
 - HIPAA
 - SOC2
 - HITRUST
 - healthcare
version: "1.0"
last-updated: "2025-11-05"
---
# ✅ **Compliance Mapping Framework**

## **Purpose**
Provide a unified mapping of security controls and prompt outputs to major compliance frameworks for healthcare and SaaS environments, ensuring alignment with regulatory and industry standards.

---

## **Included Frameworks**
- **NIST Cybersecurity Framework (CSF)** → For non-government, risk-based approach.
- **CIS Controls (IG1–IG3)** → Foundational, enterprise, and advanced implementation groups.
- **HIPAA Security Rule** → Healthcare-specific safeguards for PHI.
- **SOC 2 Trust Services Criteria** → Security, Availability, Confidentiality, Processing Integrity, Privacy.
- **HITRUST CSF** → For customer-facing compliance and healthcare assurance.

---

## **Mapping Table**
| Control Domain       | NIST CSF       | CIS IG1–IG3 | HIPAA Security Rule | SOC 2 TSC           | HITRUST CSF         |
|----------------------|---------------|-------------|----------------------|----------------------|----------------------|
| **Access Control**   | PR.AC         | IG1–IG3     | §164.312(a)(1)      | CC6.1, CC6.2        | 01.a, 01.b          |
| **Asset Management** | ID.AM         | IG1–IG2     | §164.310(d)(1)      | CC1.1               | 02.a                |
| **Audit Logging**    | DE.AE         | IG2–IG3     | §164.312(b)         | CC7.2, CC7.3        | 09.a, 09.b          |
| **Data Protection**  | PR.DS         | IG1–IG3     | §164.312(e)(1)      | CC6.6               | 08.a, 08.b          |
| **Incident Response**| RS.RP         | IG2–IG3     | §164.308(a)(6)      | CC7.4               | 11.a                |
| **Risk Management**  | ID.RA         | IG1–IG3     | §164.308(a)(1)(ii)  | CC3.2               | 12.a                |

---

## **Directive Principles**
- **Customer-Facing Items** → Include HITRUST mapping for all deliverables exposed to clients or auditors.
- **Internal Controls** → Prioritize SOC 2 and HIPAA for operational and engineering prompts.
- **Risk-Based Prioritization** → Use NIST CSF and CIS IG tiers to guide control depth.
- **Cross-Framework Consistency** → Ensure mappings align across all frameworks for unified reporting.

---

## **Usage Guidance**
- Every SOP, checklist, or template should:
  - ✅ Declare applicable frameworks in metadata.
  - ✅ Include mapped control references in the document footer.
  - ✅ Highlight gaps or overlaps between frameworks.

Example Metadata:
```
frameworks: [NIST-CSF: PR.AC, CIS: IG2, HIPAA: §164.312(a)(1), SOC2: CC6.1, HITRUST: 01.a]
```

---

## **References**
- NIST Cybersecurity Framework
- CIS Controls v8
- HIPAA Security Rule (45 CFR Part 164)
- SOC 2 Trust Services Criteria
- HITRUST CSF

---

### ✅ Key Principle:
> **Compliance mapping must be embedded in every prompt deliverable to ensure audit readiness and regulatory alignment.**
