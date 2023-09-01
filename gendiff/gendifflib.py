import json
import yaml
from gendiff.formatdiff import format_plain, format_stylish, format_json


FORMATS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


def parse_files(files):
    content = []
    for file in files:
        with open(file) as f:
            if file.endswith('json'):
                content.append(json.load(f))
            else:
                content.append(yaml.safe_load(f))
    return content


def get_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []
    for k in keys:
        if k in data1 and k in data2:
            if type(data1[k]) is dict and type(data2[k]) is dict:
                children = get_diff(data1[k], data2[k])
                diff.append({'diff': ' ', 'key': k, 'children': children})
            elif data1[k] == data2[k]:
                diff.append({'diff': ' ', 'key': k, 'value': data1[k]})
            else:
                diff.append(
                    {'diff': 'u', 'key': k, 'old': data1[k], 'new': data2[k]})
        elif k in data1:
            diff.append({'diff': '-', 'key': k, 'value': data1[k]})
        else:
            diff.append({'diff': '+', 'key': k, 'value': data2[k]})
    return diff


def generate_diff(file_path1, file_path2, format='stylish'):
    data1, data2 = parse_files([file_path1, file_path2])
    diff = get_diff(data1, data2)
    output = FORMATS[format](diff)
    return output
