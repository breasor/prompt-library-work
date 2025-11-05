---
layout: page
title: Library Index
permalink: /
---

# Prompt Library

{% assign pages = site.pages
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.name != 'index.md'" %}

{%- assign categorized   = pages | where_exp: "p", "p.category and p.category != ''" -%}
{%- assign uncategorized = pages | where_exp: "p", "p.category == nil or p.category == ''" -%}
{%- assign categories = categorized | map: "category" | uniq | sort -%}

{%- for cat in categories -%}
## {{ cat }}

{%- assign subset = categorized | where: "category", cat -%}
{%- assign with_title    = subset | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" -%}
{%- assign without_title = subset | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" -%}

<ul>
  {%- for p in with_title -%}
  <li>
    {{ p.url | relative_url }}{{ p.title | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
  {%- for p in without_title -%}
  <li>
    {{ p.url | relative_url }}{{ p.name | default: p.path | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
</ul>
{%- endfor -%}

{%- if uncategorized and uncategorized.size > 0 -%}
## Uncategorized
{%- assign with_title_u    = uncategorized | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" -%}
{%- assign without_title_u = uncategorized | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" -%}

<ul>
  {%- for p in with_title_u -%}
  <li>
    {{ p.url | relative_url }}{{ p.title | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
  {%- for p in without_title_u -%}
  <li>
    {{ p.url | relative_url }}{{ p.name | default: p.path | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
</ul>
{%- endif -%}
