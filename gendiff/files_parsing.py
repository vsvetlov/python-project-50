import json
import yaml

SUPPORTED_FORMATS = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "yml": yaml.safe_load
}


def read_file(file):
    with open(file) as f:
        content = f.read()
    return content


def parse(file, format_name):
    if format_name in SUPPORTED_FORMATS:
        content = read_file(file)
        data = SUPPORTED_FORMATS[format_name](content)
        return data
    else:
        raise Exception('Unsupported file format')


def parse_files(files):
    data = []
    for file in files:
        format_name = file.split('.')[-1]
        data.append(parse(file, format_name))
    return data
