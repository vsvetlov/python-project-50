def get_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []
    for key in keys:
        if key in data1 and key in data2:
            if type(data1[key]) is dict and type(data2[key]) is dict:
                children = get_diff(data1[key], data2[key])
                diff.append(
                    {'diff': 'nested', 'key': key, 'children': children})
            elif data1[key] == data2[key]:
                diff.append(
                    {'diff': 'unchanged', 'key': key, 'value': data1[key]})
            else:
                diff.append({'diff': 'updated', 'key': key,
                             'old': data1[key], 'new': data2[key]})
        elif key in data1:
            diff.append({'diff': 'removed', 'key': key, 'value': data1[key]})
        else:
            diff.append({'diff': 'added', 'key': key, 'value': data2[key]})
    return diff
