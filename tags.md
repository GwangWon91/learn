---
layout: page
title: Tags
permalink: /tags/
---

{% assign tags = site.tags | sort %}
{% if tags.size == 0 %}
아직 등록된 태그가 없습니다.
{% else %}
{% for tag in tags %}
<h2 id="{{ tag[0] | slugify }}">{{ tag[0] }}</h2>
<ul>
  {% for post in tag[1] %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
{% endfor %}
{% endif %}
