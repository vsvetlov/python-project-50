import argparse
import json


def get_dicts(file_path1, file_path2):
    with (
        open(file_path1) as f1,
        open(file_path2) as f2
    ):
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1, data2


def generate_diff(file_path1, file_path2):
    data1, data2 = get_dicts(file_path1, file_path2)
    keys = sorted(set(data1) | set(data2))
    diff = ['{']
    for k in keys:
        if k in data1 and k in data2:
            if data1[k] == data2[k]:
                diff.append(f'   {k}: {data1[k]}')
            else:
                diff.append(f' - {k}: {data1[k]}')
                diff.append(f' + {k}: {data2[k]}')
        elif k in data1:
            diff.append(f' - {k}: {data1[k]}')
        else:
            diff.append(f' + {k}: {data2[k]}')
    diff.append('}')
    return '\n'.join(diff)



def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()