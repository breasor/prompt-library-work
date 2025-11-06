---
layout: page
title: Library Index
permalink: "/"
---

# Prompt Library

{% comment %} Select all pages excluding the current index.md {% endcomment %}
{% assign all_pages = site.pages | where_exp: "p", "p.name != 'index.md'" %}

{% comment %} Split all pages for title-based sorting {% endcomment %}
{% assign with_title = all_pages | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" %}
{% assign without_title = all_pages | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" %}

<ul>
  {% comment %} List pages that have a title first {% endcomment %}
  {% for p in with_title %}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {% endfor %}

  {% comment %} List pages without a title last {% endcomment %}
  {% for p in without_title %}
  <li>
    <a href="{{ p.url | relative_url }}">{{ p.name | default: p.path | escape }}</a>
    <small>— ID: {{ p.id | default: "" }} | Role: {{ p.role | default: "" }} | Complexity: {{ p.complexity | default: "" }} | Version: {{ p.version | default: "" }} | Updated: {{ p["last-updated"] | default: "" }}</small>
  </li>
  {% endfor %}
</ul>
