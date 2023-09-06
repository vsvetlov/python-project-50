from gendiff.files_parsing import parse_files
from gendiff.data_parsing import get_diff
from gendiff.formatdiff import format_plain, format_stylish, format_json


FORMATS = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json
}


def generate_diff(file_path1, file_path2, format='stylish'):
    data1, data2 = parse_files([file_path1, file_path2])
    diff = get_diff(data1, data2)
    output = FORMATS[format](diff)
    return output
