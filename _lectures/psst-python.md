---
layout: page
type: lecture
date: 2022-07-27T12:59:00+3:30
title: 'Pssst! Python'
lecttag: 'Student Presentations'
hide_from_announcments: false
tldr: "Student presentations on Python Coding"
#thumbnail: /static_files/presentations/lec.jpg
#links: 
#    - url: https://github.com/jeaimehp/codeattacc-connected/blob/main/Notebook/EnviroPlus-test-example.ipynb
#      name: Pimoroni EnviroPlus Sensor Tests Jupyter Notebook
#    - url: /static_files/presentations/code.zip
#      name: codes
#    - url: https://google.com
#      name: slides
---
## Sensors Overview:
{% for team in site.data.teaminfo.connected22 %}
<div style="border-top: 2px solid black;">
<h2>Python: {{ team.pythontopic }}</h2>
<h3>Presented by: {{ team.quadname }}<h3>
<ul style="font-weight: bold;">
  <li> {{ team.duo1name }} </li>
  <li> {{ team.duo2name }} </li>
</ul>
<br>
<h3><a href=" {{ team.pythoncodeexample }}">[Sample Code]</a>
<h3>Poster</h3>
{% include image.html url=team.pythonposter width=400 %}



{% endfor %}




