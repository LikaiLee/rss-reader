import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import feedparser
import requests


class FeedsReader:
    # 超时时间
    FEED_TIMEOUT = 10
    # 最大线程数
    THREAD_NUM = 5
    # 订阅信息
    subscribes = []

    def __init__(self, subscribes, db_path):
        self.pool = ThreadPoolExecutor(max_workers=self.THREAD_NUM)
        # 订阅链接
        self.subscribes = subscribes
        # 数据文件
        self.database_file_path = os.path.join(os.getcwd(), db_path)

    def read(self):
        # 1. 读取本地数据
        database = self.__read_db()
        # 2. 读取订阅数据
        fetched = self.__read_remote()
        print()
        for new_site in fetched:
            exist_sites = [site for site in database if
                           site['url'] == new_site['url'] and site['title'] == new_site['title']]
            # 不存在该订阅网站，直接新增
            if not exist_sites:
                print('新的订阅：' + new_site['title'])
                database.append(new_site)
                continue
            # 若存在，需要对订阅的每条数据判断重复
            exist_site = exist_sites[0]
            new_feeds = []
            for new_feed in new_site['feeds']:
                if new_feed not in exist_site['feeds']:
                    new_feeds.append(new_feed)

            print(f"{exist_site['title']}: 已有 {len(exist_site['feeds'])}，"
                  f"新增 {len(new_feeds)}，"
                  f"共 {len(new_feeds) + len(exist_site['feeds'])}")
            exist_site['new_feeds'] = len(new_feeds)
            # 按倒序输出
            # 4, 5, 6 => 6, 5, 4
            exist_site['feeds'].reverse()
            # 6, 5, 4, 3, 2, 1
            exist_site['feeds'].extend(reversed(new_feeds))
            exist_site['feeds'].reverse()
        return sorted(database, key=lambda site: site['id'])

    def __read_db(self):
        """读取数据文件"""
        with open(self.database_file_path, 'r', encoding='utf-8') as fp:
            return json.loads(fp.read())

    def __read_remote(self):
        """读取订阅信息"""
        tasks = [self.pool.submit(self.__fetch_one, subscribe) for subscribe in self.subscribes]
        res = []
        for task in as_completed(tasks):
            res.append(task.result())
        self.pool.shutdown()
        return res

    def __fetch_one(self, subscribe):
        """获取一条订阅信息"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
        }
        feed = requests.get(subscribe['url'], timeout=self.FEED_TIMEOUT, headers=headers).text
        parsed_feed = feedparser.parse(feed)
        print('来自 ' + subscribe['title'] + ' 的数据: ' + str(len(parsed_feed.entries)))

        feeds = []
        for e in parsed_feed.entries:
            feeds.append({
                'title': e.title,
                'link': e.link.split('#')[0],
                'published': time.strftime('%Y-%m-%d', e.published_parsed)
            })

        return {
            'id': subscribe['id'],
            'title': subscribe['title'],
            'url': subscribe['url'],
            'feeds': feeds
        }
