import json
import yaml


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
        print(k)
        if k in data1 and k in data2:
            if type(data1[k]) is dict and type(data2[k]) is dict:
                diff.append([' ', k, get_diff(data1[k], data2[k])])
            elif data1[k] == data2[k]:
                diff.append([' ', k, data1[k]])
            else:
                diff.append(['-', k, data1[k]])
                diff.append(['+', k, data2[k]])
        elif k in data1:
            # if type(data1[k]) is dict:
            #     diff.append(['-', k, get_diff(data1[k], data1[k])])
            # else:
            diff.append(['-', k, data1[k]])
        else:
            # if type(data2[k]) is dict:
            #     diff.append(['+', k, get_diff(data2[k], data2[k])])
            # else:
            diff.append(['+', k, data2[k]])
    return diff


def dict_to_list(data):
    result = []
    for k, v in data.items():
        result.append([' ', k, v])
    return result


def format_stylish(diff, lvl=0):
    prefix = f'{" " * 4 * lvl}'
    output = ['{']
    for i in diff:
        print(i)
        if type(i[2]) is dict:
            i[2] = dict_to_list(i[2])
        if type(i[2]) is list:
            parent = format_stylish(i[2], lvl + 1)
            output.append(f'{prefix} {i[0]} {i[1]}: {parent}')
        else:
            output.append(f'{prefix} {i[0]} {i[1]}: {i[2]}')
    # output = ['{'] + [f'  {i[0]} {i[1]}: {i[2]}' for i in diff] + ['}']
    output.append(f'{prefix}}}')
    return '\n'.join(output)


def generate_diff(file_path1, file_path2):
    data1, data2 = parse_files(file_path1, file_path2)
    diff = get_diff(data1, data2)
    print(diff)
    output = format_stylish(diff)
    return output
