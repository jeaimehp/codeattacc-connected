---
type: assignment
date: 2023-07-14T13:59:00+3:30
title: 'Make it blink!'
schedtag: RPI GPIO
hide_time: true
hide_from_announcments: true
#pdf: /static_files/assignments/asg.pdf
attachment: '/Notebook/Simple Light GPIO 21.ipynb'
solutions: 'https://github.com/jeaimehp/codeattacc-connected/blob/main/Notebook/Simple%20Light%20GPIO%2021.ipynb'
due_event: 
    type: code
    date: 2023-07-14T23:59:00+3:30
    title: Additional Information 
    description: 'General Terminology'
    url: '/_images/pdf/Reference%20Document%20Connected.pdf'
    addlinktitle: LED on GPIO 21 JupyterNotebook  
    solutions: 'https://github.com/jeaimehp/codeattacc-connected/blob/main/Notebook/Simple%20Light%20GPIO%2021.ipynb'
    hide_time: true
---
# Objective
In this session, the student will connect the RPi 400 to a breadboard using an extension cable and GPIO breakout board. The student will then connect a led and resister to a GPIO pin and programmatically make it blink. 

## GPIO Breakout and Breadboard Installation

<p style="border: 4px solid red; text-align: center;"><strong style="color: red; font-size: 36px;">⚠ NOTE: When Connecting/Disconnecting the Cyberdeck and/or Enviro+, shutdown and UNPLUG the RaspberryPi 400 first!</strong></p>

## Needed Materials:

<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/Sunfounder Kit.jpeg" caption="Sunfounder Kit (Includes: breadboard, jumper wires, leds, mounting plate, GPIO breakout board, gpio header extension cable" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/Rpi-400-board-layout-1.jpeg" caption="RaspberryPi 400" width=175 align="right" %}</td>
    </tr>
</table>
 
## Final Product:

<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/Rpi_GPIObreakout.jpeg" caption="RPi with GPIO Breakout and electronics breadboard" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/LED-breadboard.jpeg" caption="LED inserted into electronics breadboard" width=175 align="right" %}</td>
    </tr>
</table>

 ---
## Video Walk Through
{% for vid in site.data.rpisetup.breadboard %}
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