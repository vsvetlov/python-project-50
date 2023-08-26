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
            if type(data1[k]) == dict and type(data2[k]) == dict:
                diff.append([' ', k, get_diff(data1[k], data2[k])])
            elif data1[k] == data2[k]:
                diff.append([' ', k, data1[k]])
            else:
                diff.append(['-', k, data1[k]])
                diff.append(['+', k, data2[k]])
        elif k in data1:
            diff.append(['-', k, data1[k]])
        else:
            diff.append(['+', k, data2[k]])
    return diff


def format_output(diff):
    output = ['{']
    for i in diff:
        print(i)
        if type(i[2]) is list:
            output.append(f'  {i[0]} {i[1]}: {format_output(i[2])}')
        else:
            output.append(f'  {i[0]} {i[1]}: {i[2]}')
    # output = ['{'] + [f'  {i[0]} {i[1]}: {i[2]}' for i in diff] + ['}']
    output.append('}')
    return '\n'.join(output)


def generate_diff(file_path1, file_path2):
    data1, data2 = parse_files(file_path1, file_path2)
    diff = get_diff(data1, data2)
    print(diff)
    output = format_output(diff)
    print(f'#####\n{output}\n###########\n###########')
    return output
