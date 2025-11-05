---
layout: page
title: Library Index
permalink: /
---

# Prompt Library

{% assign pages = site.pages
  | where_exp: "p", "p.path contains '.md'"
  | where_exp: "p", "p.name != 'index.md'" %}

{% assign categories = pages | map: "category" | uniq | sort %}

{% for cat in categories %}
## {{ cat | default: "Uncategorized" }}

<ul>
{% assign subset = pages | where: "category", cat | sort_natural: "title" %}
{% for p in subset %}
  <li>
    <a href="{{ p.urlve_url }}
      {{ p.title | default: p.name | escape }}
    </a>
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
