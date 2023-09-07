from gendiff import generate_diff
from tests.fixtures.results import stylish_result, plain_result


def test_stylish_jj():
    assert generate_diff('tests/fixtures/nfile1.json',
                         'tests/fixtures/nfile2.json') == stylish_result


def test_stylish_yy():
    assert generate_diff('tests/fixtures/nfile1.yaml',
                         'tests/fixtures/nfile2.yml') == stylish_result


def test_stylish_jy():
    assert generate_diff('tests/fixtures/nfile1.json',
                         'tests/fixtures/nfile2.yml') == stylish_result


def test_plain_jj():
    assert generate_diff('tests/fixtures/nfile1.json',
                         'tests/fixtures/nfile2.json',
                         format='plain') == plain_result


def test_json_jj():
    with open('tests/fixtures//result.json') as f1:
        result = f1.readlines()
    assert generate_diff(
        'tests/fixtures/nfile1.json', 'tests/fixtures/nfile2.json',
        format='json') == result[0]
