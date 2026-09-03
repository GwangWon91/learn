---
layout: page
title: Projects
permalink: /projects/
---

{% assign projects = site.projects | sort: "date" | reverse %}
{% if projects.size == 0 %}
아직 등록된 프로젝트가 없습니다.
{% else %}
<ul>
  {% for project in projects %}
  <li>
    <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
    {% if project.period %} — {{ project.period }}{% endif %}
  </li>
  {% endfor %}
</ul>
{% endif %}
