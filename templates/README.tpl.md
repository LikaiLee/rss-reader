# Rss-Reader

## 来源分类
{% for site in data %}
* [{{ site.title }}](#{{ site.title }}){% if site.new_feeds > 0 %} 【+{{ site.new_feeds }}】{% endif %}{% endfor %}

## 文章链接
{% for site in data %}
<details open>
    <summary id="{{ site.title }}">
     {{ site.title }}
    </summary>

{% for feed in site.feeds[:10] %}
* [【{{ feed.published }}】 {{ feed.title }}]({{ feed.link }}){% endfor %}
* [:arrow_forward: 全部文章](data/{{ site.title }}.md)
</details>
{% endfor %}

---

![build](https://github.com/LikaiLee/rss-reader/workflows/rss%20reader/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/likailee/rss-reader)
![pv](https://pageview.vercel.app/?github_user=likailee) <br>
:alarm_clock: 更新时间: {{ update_at }}