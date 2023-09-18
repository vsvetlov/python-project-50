from gendiff.data_parsing import get_diff

DIFF_MAP = {
    'nested': ' ',
    'unchanged': ' ',
    'added': '+',
    'removed': '-',
    'updated': ' '
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


def format_complex(value, lvl):
    if isinstance(value, dict):
        children = get_diff(value, value)
        stylish_children = format_stylish(children, lvl + 1)
        return stylish_children
    else:
        return format_value(value, False)


def format_stylish(diff, lvl=0):
    prefix = 4 * lvl + 1
    output = ['{']
    for node in diff:
        if node['diff'] == 'nested':
            stylish_children = format_stylish(node['children'], lvl + 1)
            output.append(
                f'{DIFF_MAP[node["diff"]]:>{prefix+2}} '
                f'{node["key"]}: {stylish_children}')
        elif node['diff'] in ['added', 'removed', 'unchanged']:
            output.append(
                f'{DIFF_MAP[node["diff"]]:>{prefix+2}} {node["key"]}: '
                f'{format_complex(node["value"], lvl)}')
        elif node['diff'] == 'updated':
            output.append(
                f'{DIFF_MAP["removed"]:>{prefix+2}} {node["key"]}: '
                f'{format_complex(node["old"], lvl)}')
            output.append(
                f'{DIFF_MAP["added"]:>{prefix+2}} {node["key"]}: '
                f'{format_complex(node["new"], lvl)}')
    output.append(f"{'}':>{prefix}}")
    return '\n'.join(output)
