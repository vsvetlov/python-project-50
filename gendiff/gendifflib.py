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
        # print(k)
        if k in data1 and k in data2:
            if type(data1[k]) is dict and type(data2[k]) is dict:
                nested_diff = get_diff(data1[k], data2[k])
                diff.append({'diff': ' ', 'key': k, 'children': nested_diff})
            elif data1[k] == data2[k]:
                diff.append({'diff': ' ', 'key': k, 'value': data1[k]})
            else:
                diff.append({'diff': '-', 'key': k, 'value': data1[k]})
                diff.append({'diff': '+', 'key': k, 'value': data2[k]})
        elif k in data1:
            diff.append({'diff': '-', 'key': k, 'value': data1[k]})
        else:
            diff.append({'diff': '+', 'key': k, 'value': data2[k]})
    return diff


def stylish(diff, lvl=0):
    prefix = f'{" " * 4 * lvl}'
    output = ['{']
    for i in diff:
        # print(i)
        if 'value' in i and type(i['value']) is dict:
            # print(f'!!!!!!!!!!!!{i}')
            i['children'] = get_diff(i['value'], i['value'])
            # print(f'*************{i}')
        if 'children' in i:
            parent = stylish(i['children'], lvl + 1)
            output.append(f'{prefix}  {i["diff"]} {i["key"]}: {parent}')
        else:
            output.append(f'{prefix}  {i["diff"]} {i["key"]}: {i["value"]}')
    # output = ['{'] + [f'  {i[0]} {i[1]}: {i[2]}' for i in diff] + ['}']
    output.append(f'{prefix}}}')
    return '\n'.join(output)


def generate_diff(file_path1, file_path2, format=stylish):
    data1, data2 = parse_files(file_path1, file_path2)
    diff = get_diff(data1, data2)
    # print(f'################\n{diff}\n###############')
    output = format(diff)
    return output
