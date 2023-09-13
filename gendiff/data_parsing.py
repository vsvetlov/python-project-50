def get_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []
    for k in keys:
        if k in data1 and k in data2:
            if type(data1[k]) is dict and type(data2[k]) is dict:
                children = get_diff(data1[k], data2[k])
                diff.append({'diff': 'complex', 'key': k, 'children': children})
            elif data1[k] == data2[k]:
                diff.append({'diff': 'unchanged', 'key': k, 'value': data1[k]})
            else:
                diff.append({'diff': 'updated', 'key': k,
                             'old': data1[k], 'new': data2[k]})
        elif k in data1:
            diff.append({'diff': 'removed', 'key': k, 'value': data1[k]})
        else:
            diff.append({'diff': 'added', 'key': k, 'value': data2[k]})
    return diff
