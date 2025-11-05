---
layout: page
title: Library Index
permalink: /
---

# Prompt Library

Auto-generated from normalized front matter. Fields: **id, title, role, category, complexity, tags, version, last-updated**.

{% assign pages = site.pages
   | where_exp: "p", "p.path contains '.md'"
   | where_exp: "p", "p.name != 'index.md'" %}

{% assign cats = pages | map: "category" | uniq | sort %}
{% for cat in cats %}
## {{ cat | default: "Uncategorized" }}

<ul>
{% assign subset = pages | where: "category", cat | sort_natural: "title" %}
{% for p in subset %}
  <li>
    <a href="{{ p.url | relative p.title | escape }}</a>
    <small>
      — <strong>ID:</strong> {{ p.id }} |
      <strong>Role:</strong> {{ p.role }} |
      <strong>Complexity:</strong> {{ p.complexity }} |
      <strong>Version:</strong> {{ p.version }} |
      <strong>Updated:</strong> {{ p.last-updated }}
      {% if p.tags and p.tags.size > 0 %} |
      <strong>Tags:</strong>
        {% for t in p.tags %}<code>{{ t }}</code>{% unless forloop.last %}, {% endunless %}{% endfor %}
      {% endif %}
    </small>
  </li>
{% endfor %}
</ul>
{% endfor %}
