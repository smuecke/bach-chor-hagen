---
layout: post
title: Intern
permalink: /intern/
nav-menu: false
show_tile: false
---

<p>Zuletzt aktualisiert am {{ "now" | date: '%d.%m.%Y' }}.</p>

<div class="row">
<div class="8u 12u$(small)">
<h2 id="termine">Terminübersicht</h2>
<p>Kommende Proben- und Konzerttermine. Unsichere oder vorläufige Angaben sind mit * markiert - aktuelle Ankündigungen auf <a href="https://bachchorhagen.slack.com">Slack</a> beachten!</p>
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
</div>
<div class="4u 12u$(small)">
<h2 id="noten">Notenmappe</h2>
<p>Aktuell werden Noten für folgende Stücke benötigt:</p>
<div class="box alt">
  <div class="row 50% uniform">
    {% for item in site.data.noten %}
      <div class="6u"><span class="image fit">
        <a href="{{ item.href }}"><img src="{{ item.src }}" alt="{{ item.alt }}"/></a>
      </span><div>
    {% endfor %}
  </div>
</div>
</div>
</div>
