from .reader.config_reader import ConfigReader
from .reader.feeds_reader import FeedsReader
from .renderer.file_renderer import FileRenderer
from .writer.feeds_writer import FeedsWriter

db_file = 'data/database.json'

print('===========读取订阅配置===========')
config_reader = ConfigReader('config/subscribe.yaml')
subscribes = config_reader.read()

print('===========读取订阅数据===========')
feeds_reader = FeedsReader(subscribes, db_file)
database = feeds_reader.read()

print('===========保存订阅数据===========')
feeds_writer = FeedsWriter(db_file)
feeds_writer.write(database)

print('===========生成最终文件===========')
renderer = FileRenderer(database)
renderer.render()
