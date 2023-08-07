---
layout: page
type: lecture
date: 2023-07-11T12:59:00+3:30
title: 'Student Collected Datasets'
lecttag: 'Prior Student Datasets - 2022'
hide_from_announcments: false
#tldr: "Student Collected Datasets"
#thumbnail: /static_files/presentations/lec.jpg
#links: 
#    - url: https://github.com/jeaimehp/codeattacc-connected/blob/main/Notebook/EnviroPlus-test-example.ipynb
#      name: Pimoroni EnviroPlus Sensor Tests Jupyter Notebook
#    - url: /static_files/presentations/code.zip
#      name: codes
#    - url: https://google.com
#      name: slides

# Ref for key as names -- https://stackoverflow.com/questions/73627320/access-yaml-key-name-with-liquid
---

{% for campyear in site.data.teaminfo%}
{% assign campname = campyear[0] | split: "-" %}
<h1> {{ campname[0] }} {{ campname[1] }}</h1> 
Combined Dataset Links from {{ campyear[1].combineddata.datasamplelocation }} on {{ campyear[1].combineddata.datasampledate }} <br> Sensor(s) used: {{ campyear[1].combineddata.datasamplesensors }}:

{% if campyear[1].combineddata.files %}

  {% for data in campyear[1].combineddata.files %}
  <br>
  <a href="{{ data.url | relative_url }}"> [ {{ data.name }} ] </a> {% if data.description %} - {{ data.description }} {% endif %} 

  {% endfor %}
<br>
{% endif%}




{% for team in campyear[1].groups %}

<div style="border-top: 2px solid black; display: flex; flex-direction: column;">
<div>
    <!-- <img src= "{{ team.teamposter | relative_url }}" > -->
</div>
<div>
<h2>Dataset Collected by: {{ team.quadname }}</h2>
<h3>Location: {{ team.datasamplelocation}} on {{ team.datasampledate }} <br> with {{ team.datasamplesensors }}</h3>

{% if team.datasets %}
  <ul>
    {% for teamdata in team.datasets %}
      <li> <strong> {{ teamdata.duo }} </strong> </li>
  
      {% for dataset in teamdata %}
          {% if forloop.first %}
          
          {% else %}
              {% assign samplename = dataset[0] | split: "_"  %}
              <a href="{{ dataset[1] | relative_url }}">[ {{ samplename[0] |capitalize }} {{ samplename[1] }} ] </a>
          {% endif %}

      {% endfor %}

  
    {% endfor %}


</ul>
{% endif %}
<br>

{% endfor %}
</div>
</div>




</div>
{% endfor %}




