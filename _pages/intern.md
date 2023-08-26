---
layout: post
title: Intern
permalink: /intern/
nav-menu: false
show_tile: false
---

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
  <div class="4u$ 12u$(small)">
    <h2 id="noten">Notenmappe</h2>
    <p>Aktuell werden Noten für folgende Stücke bei den Proben benötigt:</p>
    <div class="box alt">
      <div class="row 50% uniform">
        {% for item in site.data.noten %}
          <div class="6u"><span class="image fit">
            {% if item.href %}<a href="{{ item.href }}">{% endif %}
	      {% if item.src %}
	        <img src="{{ item.src | absolute_url }}" alt="{{ item.alt }}" title="{{ item.composer }}: {{ item.title }}"/>
	      {% else %}
		<svg width="100%" viewBox="0 0 174.09584 227.54167" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg">
    <rect style="fill:#a3c1b8" width="174.09583" height="227.54166" x="0" y="0" />
    <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:16px;font-family:serif;text-align:center;text-anchor:middle;fill:#000000" x="86.810208" y="91.46988"><tspan style="font-size:16px;text-align:center;text-anchor:middle" x="86.810208" y="91.469886">{{ item.title }}</tspan></text>
    <text xml:space="preserve" style="font-style:normal;font-weight:normal;font-size:9px;font-family:serif;text-align:center;text-anchor:middle;fill:#000000" x="86.810208" y="55.554012"><tspan style="font-size:9px;text-align:center;text-anchor:middle" x="86.810208" y="55.554012">{{ item.composer }}</tspan></text>
</svg>
	      {% endif %}
	    {% if item.href %}</a>{% endif %}
          </span></div>
        {% endfor %}
      </div>
    </div>
  </div>
</div>
<hr class="major" />
<p>Zuletzt aktualisiert am {{ "now" | date: '%d.%m.%Y' }}.</p>
