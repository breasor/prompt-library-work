---
layout: page
title: Library Index
permalink: "/"
---

# Prompt Library

{% comment %}
  Step 1: Create empty lists to hold our pages.
{% endcomment %}
{% assign categorized_pages = "" | split: "" %}
{% assign uncategorized_pages = "" | split: "" %}
{% assign categories = "" | split: "" %}

{% comment %}
  Step 2: Loop through all pages.
  Filter out the index, feed, and scss files.
  Sort pages into 'categorized' or 'uncategorized' lists.
{% endcomment %}
{% for p in site.pages %}
  {% unless p.name == 'index.md' or p.name == 'feed.xml' or p.name == 'main.scss' %}
    {% if p.category and p.category != '' %}
      {% assign categorized_pages = categorized_pages | push: p %}
      {% assign categories = categories | push: p.category %}
    {% else %}
      {% assign uncategorized_pages = uncategorized_pages | push: p %}
    {% endif %}
  {% endunless %}
{% endfor %}

{% comment %}
  Step 3: Get a unique, sorted list of category names.
{% endcomment %}
{% assign categories = categories | uniq | sort %}


{% comment %}
  Step 4: Loop through each category and list its pages.
{% endcomment %}
{% for cat in categories %}
  <h2>{{ cat }}</h2>

  {% assign subset_with_title = "" | split: "" %}
  {% assign subset_without_title = "" | split: "" %}

  {% comment %} Sort pages within this category (subset) {% endcomment %}
  {% for p in categorized_pages %}
    {% if p.category == cat %}
      {% if p.title and p.title != '' %}
        {% assign subset_with_title = subset_with_title | push: p %}
      {% else %}
        {% assign subset_without_title = subset_without_title | push: p %}
      {% endif %}
    {% endif %}
  {% endfor %}

  {% assign subset_with_title = subset_with_title | sort_natural: 'title' %}
  {% assign subset_without_title = subset_without_title | sort_natural: 'name' %}

  <ul>
    {% for p in subset_with_title %}
    <li>
      <a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a>
    </li>
    {% endfor %}
    {% for p in subset_without_title %}
    <li>
      <a href="{{ p.url | relative_url }}">{{ p.name | default: p.path | escape }}</a>
    </li>
    {% endfor %}
  </ul>
{% endfor %}


{% comment %}
  Step 5: List all uncategorized pages at the end.
{% endcomment %}
{% if uncategorized_pages.size > 0 %}
  <h2>Uncategorized</h2>

  {% assign uncategorized_with_title = "" | split: "" %}
  {% assign uncategorized_without_title = "" | split: "" %}

  {% for p in uncategorized_pages %}
    {% if p.title and p.title != '' %}
      {% assign uncategorized_with_title = uncategorized_with_title | push: p %}
    {% else %}
      {% assign uncategorized_without_title = uncategorized_without_title | push: p %}
    {% endif %}
  {% endfor %}

  {% assign uncategorized_with_title = uncategorized_with_title | sort_natural: 'title' %}
  {% assign uncategorized_without_title = uncategorized_without_title | sort_natural: 'name' %}

  <ul>
    {% for p in uncategorized_with_title %}
    <li>
      <a href="{{ p.url | relative_url }}">{{ p.title | escape }}</a>
    </li>
    {% endfor %}
    {% for p in uncategorized_without_title %}
    <li>
      <a href="{{ p.url | relative_url }}">{{ p.name | default: p.path | escape }}</a>
    </li>
    {% endfor %}
  </ul>
{% endif %}
