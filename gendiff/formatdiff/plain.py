from gendiff.formatdiff import format_value


def format_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return format_value(value)


def format_plain(diff, path=''):
    output = []
    for node in diff:
        property = '.'.join([path, node['key']]) if path else node['key']
        if node['diff'] == 'nested':
            output.append(format_plain(node['children'], property))
        elif node['diff'] == 'added':
            output.append(
                f"Property '{property}' was added with value: "
                f"{format_complex(node['value'])}")
        elif node['diff'] == 'removed':
            output.append(
                f"Property '{property}' was removed")
        elif node['diff'] == 'updated':
            output.append(
                f"Property '{property}' was updated. "
                f"From {format_complex(node['old'])} to "
                f"{format_complex(node['new'])}")
    return '\n'.join(output)
