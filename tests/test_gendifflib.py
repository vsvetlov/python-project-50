from gendiff import generate_diff

diff12 = '''{
  - follow: false
    host: hexlet.io
  - proxy: [123, 234, 53, 22]
  - timeout: {
        tag: 50
    }
  + timeout: 20
  + verbose: true
}'''

diff21 = '''{
  + follow: false
    host: hexlet.io
  + proxy: [123, 234, 53, 22]
  - timeout: 20
  + timeout: {
        tag: 50
    }
  - verbose: true
}'''

diff12y = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

diff21y = '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''

ndiff12 = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      + setting2: 23
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
      - setting7: to be removed
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

ndiff12p = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was updated. From 200 to '23'
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'common.setting7' was removed
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


path = 'tests/fixtures/'


def test_generate_diff12():
    assert generate_diff(f'{path}file1.json', f'{path}file2.json') == diff12


def test_generate_diff21():
    assert generate_diff(f'{path}file2.json', f'{path}file1.json') == diff21


def test_generate_diff12_yml():
    assert generate_diff(f'{path}file1.yml', f'{path}file2.yml') == diff12y


def test_generate_diff21_yml():
    assert generate_diff(f'{path}file2.yml', f'{path}file1.yml') == diff21y


def test_generate_ndiff12():
    assert generate_diff(f'{path}nfile1.json', f'{path}nfile2.json') == ndiff12


def test_generate_ndiff12yj():
    assert generate_diff(f'{path}nfile1.json', f'{path}nfile2.yml') == ndiff12


def test_generate_ndiff12p():
    assert generate_diff(
        f'{path}nfile1.json', f'{path}nfile2.json', format='plain') == ndiff12p


def test_generate_ndiff12j():
    with open(f'{path}/dataset.json') as f1:
        dataset = f1.readlines()
    assert generate_diff(
        f'{path}nfile1.json', f'{path}nfile2.json', format='json') == dataset[0]
