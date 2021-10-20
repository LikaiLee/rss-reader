from server.config_reader import ConfigReader
from server.feeds_reader import FeedsReader

# 读取订阅源
config_reader = ConfigReader('config/subscribe.yaml')
feeds = config_reader.read()
# 读取 RSS
feeds_reader = FeedsReader(feeds)
feeds_results = feeds_reader.read()

for e in feeds_results:
    print(e)
