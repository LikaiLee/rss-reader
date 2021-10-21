# Rss-Reader

## 来源分类
{% for site in data %}
* [{{ site.title }}](#{{ site.title }}){% endfor %}

## 文章链接
{% for site in data %}
<details open>
    <summary id="{{ site.title }}">
     {{ site.title }}
    </summary>

{% for feed in site.feeds[:10] %}
* [【{{ feed.published }}】 {{ feed.title }}]({{ feed.link }}){% endfor %}
* [......【查看更多】......](data/{{ site.title }}.md)
</details>
{% endfor %}
