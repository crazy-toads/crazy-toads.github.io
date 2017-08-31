---
layout: page
title: "Cercles"
permalink: "/cercles/"
description: "Classement par categories"
comments: false
sitemap: false
category: base
---

{% capture site_categories %}{% for cercle in site.categories %}{{ cercle | first }}{% unless forloop.last %},{% endunless %}{% endfor %}{% endcapture %}
{% assign categories_list = site_categories | split:',' | sort %}

{% for item in (0..site.categories.size) %}{% unless forloop.last %}
  {% capture this_word %}{{ categories_list[item] | strip_newlines }}{% endcapture %}
<h2 id="{{ this_word }}">{{ this_word }}</h2>
<ul class="post-list">
  {% for post in site.categories[this_word] %}{% if post.title != null %}
  <li><a href="{{ site.url }}{{ post.url }}">{{ post.title }}<span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date_to_string }}</time></span></a>
  <div class="description">
  {{ post.description | markdownify | remove: '<p>' | remove: '</p>' }}
  <a href="{{ site.url }}{{ post.url }}" class="readmore">lire la suite</a>
  </div>
  </li>
  {% endif %}{% endfor %}
  </ul>
{% endunless %}{% endfor %}

