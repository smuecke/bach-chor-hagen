---
layout: post
title: Intern
permalink: /intern/
nav-menu: false
show_tile: false
---

Zuletzt aktualisiert am {{ "now" | date: '%d.%m.%Y' }}.

## Terminübersicht

Kommende Proben- und Konzerttermine.
Unsichere oder vorläufige Angaben sind mit \* markiert - aktuelle Ankündigungen auf [Slack](https://bachchorhagen.slack.com) beachten!

<table>
<tbody>
  {% for item in site.data.termine %}
    <tr>
      {% if item.canceled %}
        <td style="color:gray"><del>{{ item.weekday }}</del></td>
        <td style="color:gray"><del>{{ item.date }}, {{ item.time }}</del></td>
        <td><b style="color:gray">fällt aus</b></td>
      {% else %}
        {% if item.weekday != "Mittwoch" or item.important %}
          <td><b>{{ item.weekday }}</b></td>
        {% else %}
          <td>{{ item.weekday }}</td>
        {% endif %}
        <td>{% if item.important %}<b>{% endif %}{{ item.date }}, {{ item.time }}{%if item.important %}</b>{% endif %}</td>
        <td>{% if item.important %}<b>{% endif %}{{ item.notes }}{%if item.important %}</b>{% endif %}</td>
      {% endif %}
    </tr>
  {% endfor %}
</tbody>
</table>

## Notenmappe

Aktuell werden Noten für folgende Stücke benötigt:

* [Jan Dismas Zelenka: Missa *Omnium Sanctorum*](https://www.alle-noten.de/Chor/Gemischter-Chor/Missa-Omnium-Sanctorum-nr-8.html?listtype=search&searchparam=missa%20omnium%20sanctorum)
