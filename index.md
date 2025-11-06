---
layout: page
title: Library Index
permalink: "/"
---

# Prompt Library

{% comment %} Select all pages excluding the current index.md {% endcomment %}
{% assign all_pages = site.pages | where_exp: "p", "p.name != 'index.md'" %}

{% comment %} Separate pages with a 'category' front matter key that is not empty {% endcomment %}
{% assign categorized = all_pages | where_exp: "p", "p.category and p.category != ''" %}

{% comment %} Separate pages without a 'category' key or with an empty value {% endcomment %}
{% assign uncategorized = all_pages | where_exp: "p", "p.category == nil or p.category == ''" %}

{% comment %} Extract unique, sorted category names {% endcomment %}
{% assign categories = categorized | map: "category" | uniq | sort %}

{% for cat in categories %}
## {{ cat }}

{% assign subset = categorized | where: "category", cat %}

{% comment %} Split the subset for title-based sorting {% endcomment %}
{% assign with_title = subset | where_exp: "p", "p.title and p.title != ''" | sort_natural: "title" %}
{% assign without_title = subset | where_exp: "p", "p.title == nil or p.title == ''" | sort_natural: "name" %}

