import json
import yaml
from gendiff.diffformat.stylish import format_stylish, format_plain


def parse_files(file_path1, file_path2):
    with (
        open(file_path1) as f1,
        open(file_path2) as f2
    ):
        if file_path1.endswith('json'):
            data1 = json.load(f1)
            data2 = json.load(f2)
        else:
            data1 = yaml.safe_load(f1)
            data2 = yaml.safe_load(f2)
    return data1, data2


def get_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []
    print(keys)
    for k in keys:
        if k in data1 and k in data2:
            if type(data1[k]) is dict and type(data2[k]) is dict:
                nested_diff = get_diff(data1[k], data2[k])
                diff.append({'diff': ' ', 'key': k, 'children': nested_diff})
            elif data1[k] == data2[k]:
                diff.append({'diff': ' ', 'key': k, 'value': data1[k]})
            else:
                diff.append({'diff': 'u', 'key': k, 'old': data1[k], 'new': data2[k]})
        elif k in data1:
            diff.append({'diff': '-', 'key': k, 'value': data1[k]})
        else:
            diff.append({'diff': '+', 'key': k, 'value': data2[k]})
    return diff


def generate_diff(file_path1, file_path2, format='stylish'):
    data1, data2 = parse_files(file_path1, file_path2)
    diff = get_diff(data1, data2)
    print(f'diff = {diff}')
    formats = {
        'stylish': format_stylish,
        'plain': format_plain
    }
    output = formats[format](diff)
    return output
