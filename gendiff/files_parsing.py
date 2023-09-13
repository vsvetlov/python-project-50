import json
import yaml

SUPPORTED_FORMATS = {
    "json": "json",
    "yaml": "yaml",
    "yml": "yaml"
}


def parse(content, format_name):
    if format_name == 'json':
        data = json.loads(content)
    elif format_name == 'yaml':
        data = yaml.safe_load(content)
    return data


def read_file(file):
    with open(file) as f:
        content = f.read()
    return content


def parse_files(files):
    data = []
    for file in files:
        file_format = file.split('.')[-1]
        if file_format in SUPPORTED_FORMATS:
            content = read_file(file)
            data.append(parse(content, SUPPORTED_FORMATS[file_format]))
        else:
            raise Exception('Unsupported file format')
    return data
