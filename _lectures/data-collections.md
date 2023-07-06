---
layout: page
type: lecture
date: 2023-07-11T12:59:00+3:30
title: 'BFL Datasets'
lecttag: 'Prior Student Datasets - 2022'
hide_from_announcments: false
tldr: "Student collected datasets 2022"
#thumbnail: /static_files/presentations/lec.jpg
#links: 
#    - url: https://github.com/jeaimehp/codeattacc-connected/blob/main/Notebook/EnviroPlus-test-example.ipynb
#      name: Pimoroni EnviroPlus Sensor Tests Jupyter Notebook
#    - url: /static_files/presentations/code.zip
#      name: codes
#    - url: https://google.com
#      name: slides
---
## Student Datasets:

**Combined Dataset Links from Brackenridge Field Laboratory on July 26, 2022:**
- [Site 1 (csv)](https://github.com/jeaimehp/codeattacc-connected/blob/main/static_files/group_datasets/connected22/site-1_all.csv)
- [Site 2 (csv)](https://github.com/jeaimehp/codeattacc-connected/blob/main/static_files/group_datasets/connected22/site-2_all.csv)
- [Site 3 (csv)](https://github.com/jeaimehp/codeattacc-connected/blob/main/static_files/group_datasets/connected22/site-3_all.csv)
- [Site 4 (csv)](https://github.com/jeaimehp/codeattacc-connected/blob/main/static_files/group_datasets/connected22/site-4_all.csv)
- [All Datasets (zip)](https://github.com/jeaimehp/codeattacc-connected/blob/main/static_files/group_datasets/connected22/all-site-datasets.zip)


{% for team in site.data.teaminfo.connected22 %}
<div style="border-top: 2px solid black;">
<h2>Dataset Collected by: {{ team.quadname }}</h2>
{% include image.html url=team.teamposter width=200 align="right" %}
<h3>Location: {{ team.datasamplelocation}} on {{ team.datasampledate }} <br> with {{ team.datasamplesensors }}</h3>




<ul style="font-weight: bold;">
  <li> {{ team.duo1name }} </li>
    <ul>
    {% if team.duo1data_site1 %}
      <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo1data_site1 }}">[Site 1 (csv)]</a></li>
    {% endif %}
    {% if team.duo1data_site2 %}
     <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo1data_site2 }}">[Site 2 (csv)]</a> </li>
    {% endif %}
    {% if team.duo1data_site3 %}
      <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo1data_site3 }}">[Site 3 (csv)]</a> </li>
    {% endif %}
    {% if team.duo1data_site4 %}
      <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo1data_site4 }}">[Site 4 (csv)]</a> </li>
    {% endif %}
    </ul>
  <li> {{ team.duo2name }} </li>
    <ul>
    {% if team.duo2data_site1 %}
      <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo2data_site1 }}">[Site 1 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site2 %}
     <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo2data_site2 }}">[Site 2 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site3 %}
      <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo2data_site3 }}">[Site 3 (csv)]</a> </li>
    {% endif %}
    {% if team.duo2data_site4 %}
     <li><a href="https://github.com/jeaimehp/codeattacc-connected/blob/main{{ team.duo2data_site4 }}">[Site 4 (csv)]</a> </li>
    {% endif %}
    </ul>
</ul>
<br>
</div>
{% endfor %}




