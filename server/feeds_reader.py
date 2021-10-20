import queue
from multiprocessing import Queue
from threading import Thread

import feedparser
import requests


class FeedsReader:
    # 超时时间
    FEED_TIMEOUT = 10
    # 最大线程数
    THREAD_NUM = 5
    # 订阅信息
    __feeds = []

    def __init__(self, feeds):
        self.__feeds = feeds

    def read(self):
        """读取订阅信息"""
        # 将订阅链接放入任务队列
        work_queue = Queue()
        for feed in self.__feeds:
            work_queue.put(feed)
        # 结果集
        results_queue = Queue()

        # 多线程获取订阅信息并放入结果集中
        workers = []
        for i in range(min(self.THREAD_NUM, len(self.__feeds))):
            worker = Thread(target=self.__fetch_urls, args=(work_queue, results_queue))
            worker.start()
            workers.append(worker)

        for worker in workers:
            worker.join()

        results = []
        while not results_queue.empty():
            results.append(results_queue.get())
        return results

    def __fetch_urls(self, work_queue: Queue, results_queue: Queue):
        """从任务队列中拉取订阅信息，并将结果放入结果集中"""
        while not work_queue.empty():
            try:
                feed_info = work_queue.get(block=False)
            except queue.Empty:
                break

            # 获取订阅信息
            feed = requests.get(feed_info['url'], timeout=self.FEED_TIMEOUT).text
            parsed_feed = feedparser.parse(feed)
            print(feed_info['title'] + ': ' + str(len(parsed_feed.entries)))
            for e in parsed_feed.entries:
                results_queue.put(e)
