---
layout: page
title: Library Index
permalink: /
---

# Prompt Library

{%- comment -%} Collect all Markdown pages except this index {%- endcomment -%}
{% assign pages = site.pages
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.name != 'index.md'" %}

{%- comment -%} Split categorized vs uncategorized (avoid nil in sort) {%- endcomment -%}
{% assign categorized   = pages | where_exp: "p", "p.category and p.category != ''" %}
{% assign uncategorized = pages | where_exp: "p", "p.category == nil or p.category == ''" %}

{%- comment -%} Build distinct category list safely {%- endcomment -%}
{% assign categories = categorized | map: "category" | uniq | sort %}

{%- for cat in categories -%}
## {{ cat }}

{%- assign subset = categorized | where: "category", cat -%}

{%- comment -%} Split by title presence to avoid sorting nil {%- endcomment -%}
{% assign with_title    = subset | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" %}
{% assign without_title = subset | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" %}

<ul>
  {%- for p in with_title -%}
  <li>
    {{ p.url | relative_url }}{{ p.title | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {%- if p.tags and p.tags.size > 0 -%} |
        <strong>Tags:</strong>
        {%- for t in p.tags -%}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{%- endfor -%}
      {%- endif -%}
    </small>
  </li>
  {%- endfor -%}

  {%- for p in without_title -%}
  <li>
    {{ p.url | relative_url }}{{ p.name | default: p.path | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {%- if p.tags and p.tags.size > 0 -%} |
        <strong>Tags:</strong>
        {%- for t in p.tags -%}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{%- endfor -%}
      {%- endif -%}
    </small>
  </li>
  {%- endfor -%}
</ul>
{%- endfor -%}

{%- if uncategorized and uncategorized.size > 0 -%}
## Uncategorized

{% assign with_title_u    = uncategorized | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" %}
{% assign without_title_u = uncategorized | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" %}

<ul>
  {%- for p in with_title_u -%}
  <li>
    <a href="{{ p.url | relative p.title | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {%- if p.tags and p.tags.size > 0 -%} |
        <strong>Tags:</strong>
        {%- for t in p.tags -%}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{%- endfor -%}
      {%- endif -%}
    </small>
  </li>
  {%- endfor -%}

  {%- for p in without_title_u -%}
  <li>
    {{ p.url | relative_url }}{{ p.name | default: p.path | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {%- if p.tags and p.tags.size > 0 -%} |
        <strong>Tags:</strong>
        {%- for t in p.tags -%}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{%- endfor -%}
      {%- endif -%}
    </small>
  </li>
  {%- endfor -%}
</ul>
{%- endif -%}
