import feedparser
from server.config_reader import read

# 读取订阅源
subscribes = read()
for rss in subscribes:
    page_dict = feedparser.parse(rss['url'])
    print(page_dict)

