from gendiff import generate_diff

diff12 = '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''

diff21 = '''{
 + follow: False
   host: hexlet.io
 + proxy: 123.234.53.22
 - timeout: 20
 + timeout: 50
 - verbose: True
}'''

path = 'tests/fixtures/'


def test_generate_diff12():
    assert generate_diff(f'{path}file1.json', f'{path}file2.json') == diff12


def test_generate_diff21():
    assert generate_diff(f'{path}file2.json', f'{path}file1.json') == diff21
