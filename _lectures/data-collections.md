---
layout: page
type: lecture
date: 2022-07-26T12:59:00+3:30
title: 'BFL Datasets'
lecttag: 'Student Datasets'
hide_from_announcments: false
tldr: "Student collected datasets"
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
<h2>Dataset Collected by: {{ team.quadname }}</h2>
{% include image.html url=team.teamposter width=200 align="right" %}
<h3>Location: {{ team.datasamplelocation}} on {{ team.datasampledate }} <br> with {{ team.datasamplesensors }}</h3>




<ul style="font-weight: bold;">
  <li> {{ team.duo1name }} </li>
    <ul>
    {% if team.duo1data_site1 %}
      <li><a href=" {{ team.duo1data_site1 }}">[Site 1 (csv)]</a></li>
    {% endif %}
    {% if team.duo1data_site2 %}
     <li><a href=" {{ team.duo1data_site2 }}">[Site 2 (csv)]</a> </li>
    {% endif %}
    {% if team.duo1data_site3 %}
      <li><a href=" {{ team.duo1data_site3 }}">[Site 3 (csv)]</a> </li>
    {% endif %}
    {% if team.duo1data_site4 %}
      <li><a href=" {{ team.duo1data_site4 }}">[Site 4 (csv)]</a> </li>
    {% endif %}
    </ul>
  <li> {{ team.duo2name }} </li>
    <ul>
    {% if team.duo2data_site1 %}
      <li><a href=" {{ team.duo2data_site1 }}">[Site 1 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site2 %}
     <li><a href=" {{ team.duo2data_site2 }}">[Site 2 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site3 %}
      <li><a href=" {{ team.duo2data_site3 }}">[Site 3 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site4 %}
     <li><a href=" {{ team.duo2data_site4 }}">[Site 4 (csv)]</a> </li>
    {% endif %}
    </ul>
</ul>
<br>
</div>
{% endfor %}




