# {{ site.title }}

{% for feed in site.feeds %}
* [{{ feed.published }}  {{ feed.title }}]({{ feed.link }}){% endfor %}