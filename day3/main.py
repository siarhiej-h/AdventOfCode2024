import re


def part_one():
    data = read_input()
    regex_pattern = r"mul\((?P<n1>\d+),(?P<n2>\d+)\)"
    matches = re.finditer(regex_pattern, data)
    total = 0
    for match in matches:
        left_arg = int(match.group('n1'))
        right_arg = int(match.group('n2'))
        total += left_arg * right_arg

    print(total)


def part_two():
    regex_pattern = r"(?P<disable>don't\(\))|(?P<enable>do\(\))|(mul\((?P<n1>\d+),(?P<n2>\d+)\))"
    data = read_input()
    matches = re.finditer(regex_pattern, data)
    total = 0
    enabled = True
    for match in matches:
        if match.group('disable'):
            enabled = False
            continue
        if match.group('enable'):
            enabled = True
            continue
        if not enabled:
            continue
        left_arg = int(match.group('n1'))
        right_arg = int(match.group('n2'))
        total += left_arg * right_arg

    print(total)


def read_input():
    with open('input.txt', 'r') as file:
        data = file.read()

    return data


if __name__ == '__main__':
    part_one()
    part_two()