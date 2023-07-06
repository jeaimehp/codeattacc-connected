---
layout: page
type: lecture
date: 2023-07-12T12:59:00+3:30
title: Sensors Overview (Enviro + Air Quality)
lecttag: 'Student Presentations'
hide_from_announcments: false
tldr: "Student presentations on used sensors"
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
<h2>{{ team.sensortype }}</h2>
<h3>Presented by: {{ team.sensornmixedquadname }}<h3>
<ul style="font-weight: bold;">
  <li> {{ team.sensorduo1 }} </li>
  <li> {{ team.sensorduo2 }} </li>
</ul>
<br>
<h3>Poster</h3>
{% include image.html url=team.sensorposter width=400 %}



{% endfor %}




