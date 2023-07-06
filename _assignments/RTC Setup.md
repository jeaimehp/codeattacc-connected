---
type: assignment
date: 2023-07-10T14:59:00+3:30
title: 'Real-time Clock PCF85232 Setup'
schedtag: Sensor
hide_time: true
hide_from_announcments: true
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: code
    date: 2023-07-10T23:59:00+3:30
    title: References 
    description: 'Real-Time Clock (RTC) PCF85232 Setup'
    url: 'https://learn.adafruit.com/adafruit-pcf8523-real-time-clock/'
    addlinktitle: 'RTC setup Reference'
    solutions: '/_images/pdf/adding-a-real-time-clock-to-raspberry-pi.pdf'
    hide_time: true
---
## Real-time Clock PCF85232 Setup
<p style="border: 4px solid red; text-align: center;"><strong style="color: red; font-size: 36px;">⚠ NOTE: When Connecting/Disconnecting the Cyberdeck and/or Enviro+, shutdown and UNPLUG the RaspberryPi 400 first!</strong></p>

## Needed Materials:



<table>
    <tr>
        <td>{% include image.html url="/_images/build-pictures/rtcbuildparts.png" href="/_images/pdf/adding-a-real-time-clock-to-raspberry-pi.pdf" caption="1. Adafruit Cyberdeck with STEMMA QT 2. CR1220 Coin Cell Battery 3. STEMMA QT male/male connector cable4. Adafruit PCF8523 RTC with STEMMA QT Module" width=175 align="right" %}
        </td>
        
    </tr>

</table>

## Final Product:

 {% include image.html url="/_images/build-pictures/rtcandcyberdeck.png" caption="Cyberdeck and RTC connected" width=175 %}


 ---
1. Insert the CR1220 Coin Cell Battery into the battery holder of the PCF8523 RTC Module with the positive (+) side of the battery away from the circuit board.

2. Insert onside of the STEMMA QT cable with the flat side of the connector away from the circuit board into either of the two STEMMA QT connectors ports on the PCF8523 RTC module.

3. Plug the other end of the STEMMA QT cable with the flat side of the connector away from the circuit board into either of the two STEMMA QT connector ports of the Cybedeck board.  


