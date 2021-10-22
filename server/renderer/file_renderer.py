import time

from jinja2 import Environment, FileSystemLoader

from server.util.file_utils import writer


class FileRenderer:

    def __init__(self, database):
        self.database = database

    def render(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('README.tpl.md')
        update_at = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        content = template.render(data=self.database, update_at=update_at)
        # README.md
        writer('README.md', content)
        # 所有订阅内容
        for site in self.database:
            feeds_tpl = env.get_template('feeds.tpl.md')
            feeds_content = feeds_tpl.render(site=site)
            writer(f"data/{site['title']}.md", feeds_content)
