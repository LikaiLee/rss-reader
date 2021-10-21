import json
import os


class FeedsWriter:

    def __init__(self, path):
        self.database_file_path = os.path.join(os.getcwd(), path)

    def write(self, database):
        with open(self.database_file_path, 'w', encoding='utf-8') as fp:
            json.dump(database, fp, ensure_ascii=False, indent=4)
