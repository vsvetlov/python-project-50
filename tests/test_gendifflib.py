from gendiff import generate_diff

diff12 = '''{
  - follow: False
    host: hexlet.io
  - proxy: [123, 234, 53, 22]
  - timeout: {
        tag: 50
    }
  + timeout: 20
  + verbose: True
}'''

diff21 = '''{
  + follow: False
    host: hexlet.io
  + proxy: [123, 234, 53, 22]
  - timeout: 20
  + timeout: {
        tag: 50
    }
  - verbose: True
}'''

diff12y = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}'''

diff21y = '''{
  + follow: False
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: True
}'''

ndiff12 = '''{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''

path = 'tests/fixtures/'


def test_generate_diff12():
    assert generate_diff(f'{path}file1.json', f'{path}file2.json') == diff12


def test_generate_diff21():
    assert generate_diff(f'{path}file2.json', f'{path}file1.json') == diff21


def test_generate_diff12_yml():
    assert generate_diff(f'{path}file1.yml', f'{path}file2.yml') == diff12y


def test_generate_diff21_yml():
    assert generate_diff(f'{path}file2.yml', f'{path}file1.yml') == diff21y


# def test_generate_ndiff12():
    # assert generate_diff(f'{path}file1.json', f'{path}file2.json') == diff12