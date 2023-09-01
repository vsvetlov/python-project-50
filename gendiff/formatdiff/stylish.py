import gendiff.gendifflib


def format_value(value, quotes=True):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif quotes and isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def format_stylish(diff, lvl=0, brackets=True):
    prefix = 4 * lvl + 1
    output = []
    for i in diff:
        if i['diff'] == 'u':
            updated_entry = [
                {'diff': '-', 'key': i['key'], 'value': i['old']},
                {'diff': '+', 'key': i['key'], 'value': i['new']}
            ]
            output.append(
                f'{format_stylish(updated_entry, lvl, False)}')
        else:
            if 'value' in i and type(i['value']) is dict:
                i['children'] = gendiff.gendifflib.get_diff(
                    i['value'], i['value'])
            if 'children' in i:
                children = format_stylish(i['children'], lvl + 1)
                output.append(f'{i["diff"]:>{prefix+2}} {i["key"]}: {children}')
            else:
                output.append(
                    f'{i["diff"]:>{prefix+2}} {i["key"]}: '
                    f'{format_value(i["value"], False)}')
    if brackets:
        output.insert(0, '{')
        output.append(f"{'}':>{prefix}}")
    return '\n'.join(output)
