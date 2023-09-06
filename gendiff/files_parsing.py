import json
import yaml


def parse_files(files):
    content = []
    for file in files:
        with open(file) as f:
            if file.endswith('json'):
                content.append(json.load(f))
            else:
                content.append(yaml.safe_load(f))
    return content
