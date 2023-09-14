from gendiff.data_parsing import get_diff

DIFF_MAP = {
    'nested': ' ',
    'unchanged': ' ',
    'added': '+',
    'removed': '-'
}


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
        if i['diff'] == 'updated':
            updated_entry = [
                {'diff': 'removed', 'key': i['key'], 'value': i['old']},
                {'diff': 'added', 'key': i['key'], 'value': i['new']}
            ]
            output.append(
                f'{format_stylish(updated_entry, lvl, False)}')
        else:
            if 'value' in i and type(i['value']) is dict:
                i['children'] = get_diff(i['value'], i['value'])
            if 'children' in i:
                children = format_stylish(i['children'], lvl + 1)
                output.append(
                    f'{DIFF_MAP[i["diff"]]:>{prefix+2}} '
                    f'{i["key"]}: {children}')
            else:
                output.append(
                    f'{DIFF_MAP[i["diff"]]:>{prefix+2}} {i["key"]}: '
                    f'{format_value(i["value"], False)}')
    if brackets:
        output.insert(0, '{')
        output.append(f"{'}':>{prefix}}")
    return '\n'.join(output)
