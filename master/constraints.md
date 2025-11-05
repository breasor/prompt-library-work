---
id: constraints
title: Prompt Constraints & Guardrails
role: Governance & Risk Control
category: Compliance & Operational Boundaries
complexity: Medium
output-format: Markdown
description: Defines mandatory constraints for prompt behavior, output structure, and compliance adherence in the InfoSec prompt library.
tags: [constraints, governance, compliance, infosec, risk]
version: 1.0
last-updated: 2025-11-05
---

# ✅ Prompt Constraints & Guardrails

## **Purpose**
Establish non-negotiable boundaries for prompt behavior and output generation to ensure security, compliance, and operational integrity across all InfoSec workflows.

---

## **Core Constraints**
- **No Sensitive Data Exposure**
  - Do not include real credentials, keys, or PHI in examples.
  - Use placeholders (e.g., ``, ``).
- **Compliance Alignment**
  - All outputs must reference applicable frameworks when relevant:
    - SOC 2, HIPAA, HITRUST for healthcare and SaaS.
    - NIST CSF and CIS Controls for technical hardening.
- **Audit-Ready Structure**
  - Mandatory metadata fields: `id`, `title`, `role`, `category`, `complexity`, `output-format`, `description`, `tags`, `version`, `last-updated`.
- **Clarification Logic**
  - Resolve ambiguity with **one clarifying question at a time**.
- **No Vendor Bias**
  - Recommendations must be standards-driven, not vendor-preferential.
- **Tone & Bias**
  - Maintain professional, authoritative, and mentorship tone.
  - Avoid slang, absolutes, or culturally biased language.

---

## **Technical Output Constraints**
- **Markdown Wrapping**
  - Use fenced blocks for all structured outputs.
  - For raw syntax preservation, use pre tag.
- **Validation Checklist**
  - ✅ Opening and closing backticks present.
  - ✅ Language specifier included.
  - ✅ Headers follow ATX style.
  - ✅ Compliance mapping included when applicable.
- **No Nested Fenced Blocks**
  - Avoid rendering conflicts in Markdown.

---

## **Compliance Mapping Requirement**
- Every SOP, JIRA story, or technical template must:
  - Include compliance references in Notes or footer.
  - Example:
    ```
    Compliance Mapping: [SOC 2: CC6.1], [HIPAA: §164.312(a)(1)], [NIST-CSF: PR.AC], [CIS IG2], [HITRUST: 01.a]
    ```

---

## **Risk Guardrails**
- **No Automation Without Validation**
  - Scripts or IaC must include rollback steps.
- **No Ambiguous Deliverables**
  - Outputs must be actionable and measurable.
- **No Unapproved Frameworks**
  - Stick to NIST, CIS, SOC 2, HIPAA, HITRUST unless explicitly approved.

---

## **References**
- See `tone-bias.md` for communication standards.
- See `mode-directives.md` for behavioral rules.
- See `compliance-mapping.md` for framework alignment.

---

### ✅ Key Principle:
> **Constraints are mandatory guardrails, not optional guidelines. Every prompt must comply before publishing.**
