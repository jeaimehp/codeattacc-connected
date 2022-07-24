---
type: assignment
date: 2022-07-25T12:59:00+3:30
title: 'RPi Setup and Configuration'
schedtag: Linux(Raspbian)
hide_time: true
hide_from_announcments: true
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: code
    date: 2022-07-25T23:59:00+3:30
    title: References 
    description: 'RPi Beginners Guide 4thEd English v2'
    url: '/_images/pdf/BeginnersGuide-4thEd-Eng_v2.pdf'
    addlinktitle: '7in HDMI LCD Manual'
    solutions: '/_images/pdf/7in-HDMI-LCD%20Manual.pdf'
    hide_time: true
---
## Needed Materials:



<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/HDMI Screen.jpeg" href="/_images/pdf/7in-HDMI-LCD%20Manual.pdf" caption="7in HDMI LCD Kit" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/RaspberryPI 400.jpeg" href="/_images/pdf/7in-HDMI-LCD%20Manual.pdf" caption="RaspberryPi 400" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/4Port Surge Strip.jpeg" caption="4-Port Surge Strip" width=175 align="right" %}</td>
    </tr>
</table>



## Final Product:
{% include image.html url="/_images/build-pictures/rpi_on_desk.jpeg" caption="RPi 400 on desk with attached keyboard, mouse, and 7in Screen" width=175 %}

 
 ---
## Video Walk Through

Reference - [7in HDMI LCD Manual](/_images/pdf/7in-HDMI-LCD%20Manual.pdf)

{% for vid in site.data.rpisetup.screenbuild %}
<div style="border-top: 2px solid black;">
<h2>{{ vid.name }}</h2>
{% if vid.description %}
{{ vid.description }}
{% endif %}
<a href="{{ vid.youtubelink }}">[YouTube Link]</a>
<br>

{% include youtubeembed.html  ytid=vid.embedid %}

<br>


{% endfor %}
</div>
