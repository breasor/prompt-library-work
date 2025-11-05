# ✅ Prompt Library Extension: Role-Based Schema + Starter Template

---

## **1. Metadata Schema for Role-Based Prompts**

Each prompt file must include **YAML front matter** for validation and indexing.

```yaml
---
id: <unique-id>                # e.g., seceng-hardening-001
title: <short descriptive title>
role: <security-analyst | security-engineer | security-architect | technical-writer>
category: <incident-response | automation | architecture | documentation>
complexity: <low | medium | high>
output-format: <markdown | json | xml | powershell>
description: <one-line purpose>
tags: [<keywords>]
version: 1.0
last-updated: YYYY-MM-DD
---
```

---

## **2. Folder Scaffolding**

```
prompts/
└── roles/
    ├── security-analyst/
    │   ├── threat-hunting.md
    │   ├── incident-analysis.md
    │   └── soc-reporting.md
    │
    ├── security-engineer/
    │   ├── hardening-guides.md
    │   ├── automation-scripts.md
    │   └── detection-rules.md
    │
    ├── security-architect/
    │   ├── zero-trust-design.md
    │   ├── cloud-architecture.md
    │   └── risk-modeling.md
    │
    └── technical-writer/
        ├── compliance-docs.md
        ├── sop-authoring.md
        └── policy-drafts.md
```

---

## **3. Starter Template: Security Engineer Prompt**

```markdown
---
id: seceng-hardening-001
title: Windows Server Hardening SOP Generator
role: security-engineer
category: hardening
complexity: medium
output-format: markdown
description: Generate a structured SOP for Windows Server hardening aligned with CIS benchmarks.
tags: [windows, hardening, cis, sop]
version: 1.0
last-updated: 2025-11-05
---

## **Prompt Objective**
Generate a **Windows Server Hardening SOP** with:
- CIS Benchmark alignment
- Step-by-step execution
- Validation checklist
- Rollback procedure

## **Constraints**
- Output must be wrapped in fenced block: `markdown`
- Include sections: **Title, Purpose, Scope, Procedure, Validation, Rollback**
- No generic advice; only actionable steps.

## **Example Invocation**
```
Generate a Windows Server Hardening SOP for Server 2022 using CIS Level 1 controls.
```
```

---

## **4. CI/CD Governance Updates**
- **validate-prompts.yml**:
  - Enforce presence of `role`, `category`, `complexity`, `output-format`.
- **generate-index.ps1**:
  - Add role-based grouping in index output.
- **schema-reference.md**:
  - Document new fields and validation rules.

---

### ✅ Next Steps
Do you want me to:
1. **Generate full scaffolding with placeholder files for all roles** (with metadata + stub content)?
2. **Create PowerShell script `generate-role-scaffolding.ps1`** to automate adding new roles/categories?
3. **Add GitHub Actions workflow to validate role-based schema**?

Pick **1**, **2**, or **3** (or all).
