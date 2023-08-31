import gendiff.gendifflib


def json_format(value, q=True):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif q:
        return f"'{value}'"
    else:
        return f"{value}"


def is_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return json_format(value)


def format_stylish(diff, lvl=0):
    prefix = f'{" " * 4 * lvl}'
    output = ['{']
    for i in diff:
        if i['diff'] == 'u':
            updated_entry = [
                {'diff': '-', 'key': i['key'], 'value': i['old']},
                {'diff': '+', 'key': i['key'], 'value': i['new']}
                ]
            output.append(f'{format_stylish(updated_entry, lvl)[2: -2].rstrip()}')
        else:
            if 'value' in i and type(i['value']) is dict:
                i['children'] = gendiff.gendifflib.get_diff(i['value'], i['value'])
            if 'children' in i:
                parent = format_stylish(i['children'], lvl + 1)
                output.append(f'{prefix}  {i["diff"]} {i["key"]}: {parent}')
            else:
                output.append(f'{prefix}  {i["diff"]} {i["key"]}: {json_format(i["value"], False)}')
    output.append(f'{prefix}}}')
    return '\n'.join(output)


def format_plain(diff, path=''):
    output = []
    # property = ''
    for i in diff:
        property = '.'.join([path, i['key']]) if path else i['key']
        # print([path] + [i['key']])
        if 'children' in i:
            output.append(format_plain(i['children'], property))
        elif i['diff'] == '+':
            # print(i)
            output.append(
                f"Property '{property}' was added with value: {is_complex(i['value'])}")
        elif i['diff'] == '-':
            output.append(
                f"Property '{property}' was removed")
        elif i['diff'] == 'u':
            output.append(
                f"Property '{property}' was updated. From {is_complex(i['old'])} to {is_complex(i['new'])}")
    return '\n'.join(output)
