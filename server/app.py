from server.reader.config_reader import ConfigReader
from server.reader.feeds_reader import FeedsReader
from server.renderer.readme_renderer import ReadmeRenderer
from server.writer.feeds_writer import FeedsWriter

db_file = 'data/database.json'

print('===========读取订阅配置===========')
config_reader = ConfigReader('config/subscribe.yaml')
subscribes = config_reader.read()

print('===========读取订阅数据===========')
feeds_reader = FeedsReader(subscribes, db_file)
database = feeds_reader.read()

print('===========写入订阅数据===========')
feeds_writer = FeedsWriter(db_file)
feeds_writer.write(database)

# README.md
readme_renderer = ReadmeRenderer(database)
readme_renderer.render()
