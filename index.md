---
layout: page
title: Library Index
permalink: "/"
---

# Prompt Library

{% comment %} Select all pages excluding the current index.md {% endcomment %}
{% assign all_pages = site.pages | where_exp: "p", "p.name != 'index.md'" %}

{% comment %} Separate pages with a 'category' front matter key that is not empty {% endcomment %}
{%- assign categorized = all_pages | where_exp: "p", "p.category and p.category != ''" -%}

{% comment %} Separate pages without a 'category' key or with an empty value {% endcomment %}
{%- assign uncategorized = all_pages | where_exp: "p", "p.category == nil or p.category == ''" -%}

{% comment %} Extract unique, sorted category names {% endcomment %}
{%- assign categories = categorized | map: "category" | uniq | sort -%}

{%- for cat in categories -%}
## {{ cat }}

{%- assign subset = categorized | where: "category", cat -%}

{% comment %} Split the subset for title-based sorting {% endcomment %}
{%- assign with_title = subset | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" -%}
{%- assign without_title = subset | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" -%}

<ul>
  {%- for p in with_title -%}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
  {%- for p in without_title -%}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.name | default: p.path | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
</ul>
{%- endfor -%}

{%- if uncategorized and uncategorized.size > 0 -%}
## Uncategorized

{% comment %} Split the uncategorized subset for title-based sorting {% endcomment %}
{%- assign with_title_u = uncategorized | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" -%}
{%- assign without_title_u = uncategorized | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" -%}

<ul>
  {%- for p in with_title_u -%}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
  {%- for p in without_title_u -%}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.name | default: p.path | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {%- endfor -%}
</ul>
{%- endif -%}
