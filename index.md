---
layout: page
title: Library Index
permalink: "/"
---

# Prompt Library

{% comment %}
  First, we create empty lists to hold our pages.
{% endcomment %}
{% assign all_pages = "" | split: "" %}
{% assign with_title = "" | split: "" %}
{% assign without_title = "" | split: "" %}

{% comment %}
  Loop through all site.pages.
  We will add them to the 'all_pages' list,
  EXCEPT for 'index.md' itself.
{% endcomment %}
{% for p in site.pages %}
  {% if p.name != 'index.md' %}
    {% assign all_pages = all_pages | push: p %}
  {% endif %}
{% endfor %}

{% comment %}
  Now, loop through our 'all_pages' list
  and sort them into two new lists:
  one for pages WITH a title, one for pages WITHOUT.
{% endcomment %}
{% for p in all_pages %}
  {% if p.title and p.title != '' %}
    {% assign with_title = with_title | push: p %}
  {% else %}
    {% assign without_title = without_title | push: p %}
  {% endif %}
{% endfor %}

{% comment %}
  Finally, sort the lists alphabetically.
{% endcomment %}
{% assign with_title = with_title | sort_natural: "title" %}
{% assign without_title = without_title | sort_natural: "name" %}

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
