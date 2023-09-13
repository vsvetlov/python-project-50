import os
from pytest import mark
from gendiff import generate_diff
from tests.fixtures.results import stylish_result, plain_result


filesets = [
    ('nfile1.json', 'nfile2.json'),
    ('nfile1.yaml', 'nfile2.yml'),
    ('nfile1.json', 'nfile2.yml')
]


abs_sets = [
    tuple(os.path.join(os.path.dirname(__file__), 'fixtures', f)
          for f in fileset) for fileset in filesets]


@mark.parametrize('file1, file2', abs_sets)
def test_stylish_(file1, file2):
    assert generate_diff(file1, file2) == stylish_result


@mark.parametrize('file1, file2', abs_sets)
def test_plain(file1, file2):
    assert generate_diff(file1, file2, format='plain') == plain_result


@mark.parametrize('file1, file2', abs_sets)
def test_json(file1, file2):
    json_file = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'result.json')
    with open(json_file) as f1:
        json_result = f1.readlines()[0]
    assert generate_diff(file1, file2, format='json') == json_result
