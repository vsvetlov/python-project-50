import gendiff.gendifflib


def format_value(value, q=True):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif q:
        return f"'{value}'"
    else:
        return f"{value}"


def format_stylish(diff, lvl=0):
    prefix = f'{" " * 4 * lvl}'
    output = ['{']
    for i in diff:
        if i['diff'] == 'u':
            updated_entry = [
                {'diff': '-', 'key': i['key'], 'value': i['old']},
                {'diff': '+', 'key': i['key'], 'value': i['new']}
            ]
            output.append(
                f'{format_stylish(updated_entry, lvl)[2: -2].rstrip()}')
        else:
            if 'value' in i and type(i['value']) is dict:
                i['children'] = gendiff.gendifflib.get_diff(
                    i['value'], i['value'])
            if 'children' in i:
                parent = format_stylish(i['children'], lvl + 1)
                output.append(f'{prefix}  {i["diff"]} {i["key"]}: {parent}')
            else:
                output.append(
                    f'{prefix}  {i["diff"]} {i["key"]}: '
                    f'{format_value(i["value"], False)}')
    output.append(f'{prefix}}}')
    return '\n'.join(output)
