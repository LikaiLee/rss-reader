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

    def __init__(self, subscribes):
        self.subscribes = subscribes
        self.pool = ThreadPoolExecutor(max_workers=self.THREAD_NUM)

    def read(self):
        """读取订阅信息"""
        tasks = [self.pool.submit(self.fetch_one, subscribe) for subscribe in self.subscribes]
        res = []
        for task in as_completed(tasks):
            res.append(task.result())
        self.pool.shutdown()
        return res

    def fetch_one(self, subscribe):
        """获取一条订阅信息"""
        feed = requests.get(subscribe['url'], timeout=self.FEED_TIMEOUT).text
        parsed_feed = feedparser.parse(feed)
        print(subscribe['title'] + ': ' + str(len(parsed_feed.entries)))
        return {
            'subscribe': subscribe,
            'feeds': parsed_feed.entries
        }
