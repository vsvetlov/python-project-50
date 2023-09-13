from gendiff.formatdiff import format_value


def format_complex(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return format_value(value)


def format_plain(diff, path=''):
    output = []
    for i in diff:
        property = '.'.join([path, i['key']]) if path else i['key']
        if 'children' in i:
            output.append(format_plain(i['children'], property))
        elif i['diff'] == 'added':
            output.append(
                f"Property '{property}' was added with value: "
                f"{format_complex(i['value'])}")
        elif i['diff'] == 'removed':
            output.append(
                f"Property '{property}' was removed")
        elif i['diff'] == 'updated':
            output.append(
                f"Property '{property}' was updated. "
                f"From {format_complex(i['old'])} to "
                f"{format_complex(i['new'])}")
    return '\n'.join(output)
