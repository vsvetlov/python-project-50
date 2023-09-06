from gendiff import generate_diff
from tests.fixtures.datasets import ndiff12, ndiff12p


def test_generate_ndiff12():
    assert generate_diff(
        'tests/fixtures/nfile1.json', 'tests/fixtures/nfile2.json') == ndiff12


def test_generate_ndiff12y():
    assert generate_diff(
        'tests/fixtures/nfile1.yaml', 'tests/fixtures/nfile2.yml') == ndiff12


def test_generate_ndiff12yj():
    assert generate_diff(
        'tests/fixtures/nfile1.json', 'tests/fixtures/nfile2.yml') == ndiff12


def test_generate_ndiff12p():
    assert generate_diff(
        'tests/fixtures/nfile1.json', 'tests/fixtures/nfile2.json',
        format='plain') == ndiff12p


def test_generate_ndiff12j():
    with open('tests/fixtures//dataset.json') as f1:
        dataset = f1.readlines()
    assert generate_diff(
        'tests/fixtures/nfile1.json', 'tests/fixtures/nfile2.json',
        format='json') == dataset[0]
