import os

import yaml


def read():
    config_file_path = os.path.join(os.getcwd(), 'config/subscribe.yaml')
    with open(config_file_path, 'r', encoding='utf-8') as f:
        subscribes = yaml.safe_load(f)
        return subscribes
