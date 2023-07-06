---
type: assignment
date: 2023-07-10T13:59:00+3:30
title: 'Developmental Enviroment Setup'
schedtag: Linux(Raspbian)
hide_time: true
hide_from_announcments: true
#pdf: /static_files/assignments/asg.pdf
#attachment: /static_files/assignments/asg.zip
#solutions: /static_files/assignments/asg_solutions.pdf
due_event: 
    type: code
    date: 2023-07-10T23:59:00+3:30
    title: Additional Information 
    description: 'General Code@TACC:Connected Reference and Terminology'
    url: '/_images/pdf/Reference%20Document%20Connected.pdf'
    #addlinktitle: 
    #solutions: 
    hide_time: true
---
**To load all needed software:**

- Within Raspbian open a Terminal window
- Type `git clone https://github.com/jeaimehp/codeattacc-connected.git`
- Type `cd codeattacc-connected`
- Type `./rpi-setup.bash`
- Press `y` and press [Enter] at any prompts. Note: The final one will restart your RPi
 
 ---
## Video Walk Through
{% for vid in site.data.rpisetup.devenvironment %}
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