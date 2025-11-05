---
layout: page
title: Library Index
permalink: /
---

# Prompt Library

{% comment %}
Collect all Markdown pages except index itself.
{% endcomment %}
{% assign pages = site.pages
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.name != 'index.md'" %}

{% comment %}
Normalize category to avoid nil comparisons later.
We'll derive a category label per page for grouping.
{% endcomment %}
{% assign categories = pages
  | map: "category"
  | uniq
  | sort %}

{% if categories.size == 0 %}
  {% assign categories = "" | split: "" %}
{% endif %}

{% for cat in categories %}
## {{ cat | default: "Uncategorized" }}

{% assign subset = pages | where: "category", cat %}

{% comment %}
Split pages with titles from those without, so we can sort safely.
{% endcomment %}
{% assign with_title = subset | where_exp: "p", "p.title" | sort_natural: "title" %}
{% assign without_title = subset | where_exp: "p", "p.title == nil" | sort_natural: "name" %}

<ul>
  {% for p in with_title %}
  <li>
    {{ p.url | relative_url }}{{ p.title | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {% if p.tags and p.tags.size > 0 %} |
        <strong>Tags:</strong>
        {% for t in p.tags %}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}
      {% endif %}
    </small>
  </li>
  {% endfor %}

  {% for p in without_title %}
  <li>
    {{ p.url | relative_url }}{{ p.name | default: p.path | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id | default: "" }}
      | <strong>Role:</strong> {{ p.role | default: "" }}
      | <strong>Complexity:</strong> {{ p.complexity | default: "" }}
      | <strong>Version:</strong> {{ p.version | default: "" }}
      | <strong>Updated:</strong> {{ p["last-updated"] | default: "" }}
      {% if p.tags and p.tags.size > 0 %} |
        <strong>Tags:</strong>
        {% for t in p.tags %}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}
      {% endif %}
    </small>
  </li>
  {% endfor %}
</ul>
{% endfor %}
``
