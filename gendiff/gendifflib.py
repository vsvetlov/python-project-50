import json


def parsing_files(file_path1, file_path2):
    with (
        open(file_path1) as f1,
        open(file_path2) as f2
    ):
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1, data2


def generate_diff(file_path1, file_path2):
    data1, data2 = parsing_files(file_path1, file_path2)
    keys = sorted(set(data1) | set(data2))
    diff = ['{']
    for k in keys:
        if k in data1 and k in data2:
            if data1[k] == data2[k]:
                diff.append(f'   {k}: {data1[k]}')
            else:
                diff.append(f' - {k}: {data1[k]}')
                diff.append(f' + {k}: {data2[k]}')
        elif k in data1:
            diff.append(f' - {k}: {data1[k]}')
        else:
            diff.append(f' + {k}: {data2[k]}')
    diff.append('}')
    return '\n'.join(diff)
