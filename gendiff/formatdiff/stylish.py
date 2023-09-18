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
    for node in diff:
        if node['diff'] == 'updated':
            updated_entry = [
                {'diff': 'removed', 'key': node['key'], 'value': node['old']},
                {'diff': 'added', 'key': node['key'], 'value': node['new']}
            ]
            output.append(
                f'{format_stylish(updated_entry, lvl, False)}')
        else:
            if 'value' in node and type(node['value']) is dict:
                node['children'] = get_diff(node['value'], node['value'])
            if 'children' in node:
                children = format_stylish(node['children'], lvl + 1)
                output.append(
                    f'{DIFF_MAP[node["diff"]]:>{prefix+2}} '
                    f'{node["key"]}: {children}')
            else:
                output.append(
                    f'{DIFF_MAP[node["diff"]]:>{prefix+2}} {node["key"]}: '
                    f'{format_value(node["value"], False)}')
    if brackets:
        output.insert(0, '{')
        output.append(f"{'}':>{prefix}}")
    return '\n'.join(output)
