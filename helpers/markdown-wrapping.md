---
id: markdown-wrapping-guidelines
title: "Markdown Wrapping Guidelines"
role: "Documentation Standard"
category: "Formatting & Output Control"
complexity: "Low"
output-format: "Markdown (with raw examples)"
description: >
  Defines rules for wrapping, fenced blocks, platform-specific encapsulation, and validation for Markdown outputs.
tags:
 - markdown
 - formatting
 - prompts
 - fenced-blocks
 - validation
version: 1.4
last-updated: 2025-11-05
---
# ✅ **Markdown Wrapping Guidelines**

## **Purpose**
Ensure consistent and error-free Markdown formatting across all prompts and outputs.
This guide defines **wrapping rules**, **fenced block usage**, and **platform-specific encapsulation**.

---

## **1. Standard Markdown Wrapping**
- **Default Rule:**
  Use **pre tag** to preserve whitespace and raw characters when showing examples or entire documents.
  This prevents Markdown rendering and ensures literal syntax is displayed correctly.

Example:
```
# Title
## Purpose
...
```

- When using fenced blocks outside pre tag, always specify the language after the opening backticks:
  - ✅ `markdown` for standard Markdown.
  - ✅ `json`, `xml`, `powershell` for alternative formats.
  - ❌ Never use `markdowwn` (typo breaks rendering).

---

## **2. Section Headers**
- Use **ATX-style headers** (`#`, `##`, `###`) for clarity.

---

## **3. Platform-Specific Encapsulation**
When targeting a specific platform, wrap content in **custom fenced blocks**:

| Platform        | Fence Syntax            |
|-----------------|-------------------------|
| **Confluence**  | ```markdown-confluence |
| **Obsidian**    | ```markdown-obsidian   |
| **GitHub Docs** | ```markdown-github     |

Example:
```
# SOP: Windows Server Hardening
## Purpose
Align with CIS benchmarks for secure configuration.
```

---

## **4. Inline Code & Lists**
- Inline code → Use single backticks: `command`.
- Lists:
  - Use `-` for unordered lists.
  - Use `1.` for ordered lists.
- Always leave **one blank line** before and after lists for proper rendering.

---

## **5. Tables**
- Use pipe syntax for tables:

```
| Column 1 | Column 2 |
|----------|----------|
| Value A  | Value B  |
```

---

## **6. Common Pitfalls**
- **Do NOT nest fenced blocks inside fenced blocks.**
- **Do NOT omit language specifier** (e.g., ```powershel → typo).
- **Do NOT mix tabs and spaces** in lists or tables.
- Always close fenced blocks with **three backticks** on a new line.

---

## **7. Validation Checklist**
Before committing a prompt:
- ✅ Opening and closing backticks present.
- ✅ Language specifier included.
- ✅ Headers follow ATX style.
- ✅ Lists and tables properly spaced.
- ✅ No nested fenced blocks.
- ✅ pre tag used for raw Markdown preservation.

---

## **References**
- See `output-formatting.md` for full examples of Markdown, JSON, XML.
- See `mode-directives.md` for behavioral rules.
