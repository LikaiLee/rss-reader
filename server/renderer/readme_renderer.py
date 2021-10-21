from jinja2 import Environment, FileSystemLoader


class ReadmeRenderer:

    def __init__(self, database):
        self.database = database

    def render(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('README.tpl.md')
        content = template.render(data=self.database)
        print(content)
