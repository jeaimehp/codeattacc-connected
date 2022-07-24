---
type: assignment
date: 2022-07-25T14:59:00+3:30
title: 'Pimoroni Enviro + Air Quality(PIM458) with Particulate Sensor'
schedtag: Sensor
hide_time: true
hide_from_announcments: true
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
        <td>{% include image.html url="/_images/build-pictures/PM25-SensorKit.JPG" href= "https://shop.pimoroni.com/products/pms5003-particulate-matter-sensor-with-cable?variant=29075640352851" caption="PMS5003 Particulate Matter(PM) Sensor with Cable" width=175 align="right" %}</td>
        
    </tr>

</table>

## Final Product:

 {% include image.html url="/_images/build-pictures/PMSensor_Cyberbeck_RPi400.JPG" caption="RPi400 with Cyberdeck and Enviro+ with PM Sensor" width=175 %}


 ---
## PMS5003 Particulate Matter(PM) Sensor Installation
[Note: The included cable breakout board (circuit board) will not be used.]

<strong style="color: red;">Do not force the cable onto the pins. This can danage the PM Sensor or Enviroplus!</strong>

<table>
    <tr><td><h2>Step 1:</h2></td></tr>
    <tr style="vertical-align: top;">
        <td>
            {% include image.html url="/_images/build-pictures/PM1.JPG" caption="Plug the ribbon cable into the blue PMS5003 Sensor with the side of the plug with the lines/metal up perpendicular to the pins closest to the edge." width=250 %}
            
        </td>
        <td>
        {% include image.html url="/_images/build-pictures/PM2.JPG" caption="Result" width=250 %}
        </td>
    </tr>
    <tr><td><h2>Step 2:</h2></td></tr>
      <tr style="vertical-align: top;">
        <td>
            {% include image.html url="/_images/build-pictures/PM3.JPG" caption="Plug the ribbon cable into the bottom of the Enviro+ Sensor with the side of the plug with the lines/metal up perpendicular to the pins closest to the edge." width=250 %}
            
        </td>
        <td>
        {% include image.html url="/_images/build-pictures/PM4.JPG" caption="Result" width=250 %}
        </td>
    </tr>
    <tr><td><h2>Step 3:</h2></td></tr>
    <tr>
        <td>
        {% include image.html url="/_images/build-pictures/PM5.JPG" caption="Plug the Enviroplus onto the Cyberdeck Pins" width=250 %}
        </td>
    </tr>
    <tr><td><h2>Step 4:</h2></td></tr>
    <tr>
        <td>
        {% include image.html url="/_images/build-pictures/PMSensor_Cyberbeck_RPi400.JPG" caption="Plug the Cyberdeck with the EnviroPlus and PMS5003 into the GPIO Pins of the RPi400" width=250 %}
        </td>
    </tr>
</table>



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
