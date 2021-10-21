# README template
{% for item in data %}
<details open>
    <summary id="{{ item.title }}">
     {{ item.title }}
    </summary>

{% for feed in item.feeds %}
- [{{ feed.published }}  {{ feed.title }}]({{ feed.link }}){% endfor %}

</details>
{% endfor %}
