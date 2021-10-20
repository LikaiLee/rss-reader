import os

import yaml


class ConfigReader:
    __path = ''

    def __init__(self, path):
        self.__path = path

    def read(self):
        """read feeds from config file"""
        config_file_path = os.path.join(os.getcwd(), self.__path)
        with open(config_file_path, 'r', encoding='utf-8') as f:
            subscribes = yaml.safe_load(f)
            return subscribes
