---
type: assignment
date: 2022-07-25T14:59:00+3:30
title: 'Pimoroni Enviro + Air Quality(PIM458) with Particulate Sensor'
schedtag: Sensor
hide_time: true
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: code
    date: 2022-07-25T23:59:00+3:30
    title: References 
    description: 'Pimoroni Enviro + Air Quality(PIM458)'
    url: 'https://shop.pimoroni.com/products/enviro?variant=31155658457171'
    #addlinktitle: '7in HDMI LCD Manual'
    #solutions: '/_images/pdf/7in-HDMI-LCD%20Manual.pdf'
    hide_time: true
---
## Enviro+ and Cyberdeck Installation
<p style="border: 4px solid red; text-align: center;"><strong style="color: red; font-size: 36px;">⚠ NOTE: When Connecting/Disconnecting the Cyberdeck and/or Enviro+, shutdown and UNPLUG the RaspberryPi 400 first!</strong></p>

## Needed Materials:



<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/RaspberryPI 400.jpeg" href="/_images/pdf/7in-HDMI-LCD%20Manual.pdf" caption="RaspberryPi 400" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/CyberDeck.jpeg" caption="Adafruit Cyberdeck" width=175 align="right" %}</td>
        <td>{% include image.html url="/_images/build-pictures/Pimoroni PIM458.jpeg" href= "https://shop.pimoroni.com/products/enviro?variant=31155658457171" caption="Pimoroni Enviro + Air Quality PIM458" width=175 align="right" %}</td>
    </tr>
</table>
 ---

## Sensor Test Code

<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/envrioPlus test.png" caption="Enviro+ Sensor Test" width=500 %} </td>
        <td> 
        <h2>Testing the Enviro+:</h2>
        <ol>
           <li> Within Raspbian open a Terminal window</li> 
           <li> Type <code>ls</code> to list(view) all files </li> 
           <li> Type <code>cd codeattacc-connected</code> and press [Enter] </li> 
           <li> Type <code>ls</code> to list(view) all files and look for <code>sensortest.bash</code> </li> 
           <li> Type <code>./sensortest.bash</code> and check the screen on your Enviro+ for information </li> 
           <li> [Note: If you receive an error of do not have a display please ask for assistance.] </li> 
        </ol>
        </td>
    </tr>
</table>

## Video Walk Through

Reference - [Pimoroni Enviro + Air Quality Getting Started](/_images/pdf/Getting%20Started%20with%20EnviroPlus.pdf)

{% for vid in site.data.rpisetup.environplus %}
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
