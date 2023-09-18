from gendiff.data_parsing import get_diff

STYLES = {
    'nested': ' ',
    'unchanged': ' ',
    'added': '+',
    'removed': '-',
    'updated': ' ',
    '}': '}'
}


def get_prefix(style, lvl):
    indent = 4 * lvl + 1
    if style == '}':
        return f'{STYLES[style]:>{indent}}'
    return f'{STYLES[style]:>{indent+2}}'


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
    output = ['{']
    for node in diff:
        if node['diff'] == 'nested':
            stylish_children = format_stylish(node['children'], lvl + 1)
            output.append(
                f'{get_prefix(node["diff"], lvl)} {node["key"]}: '
                f'{stylish_children}')
        elif node['diff'] in ['added', 'removed', 'unchanged']:
            output.append(
                f'{get_prefix(node["diff"], lvl)} {node["key"]}: '
                f'{format_complex(node["value"], lvl)}')
        elif node['diff'] == 'updated':
            output.append(
                f'{get_prefix("removed", lvl)} {node["key"]}: '
                f'{format_complex(node["old"], lvl)}')
            output.append(
                f'{get_prefix("added", lvl)} {node["key"]}: '
                f'{format_complex(node["new"], lvl)}')
    output.append(f'{get_prefix("}", lvl)}')
    return '\n'.join(output)
