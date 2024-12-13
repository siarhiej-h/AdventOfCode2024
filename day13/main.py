import re

def part_one():
    machines = read_input()
    tokens = 0
    for machine in machines:
        a = machine['a']
        b = machine['b']
        prize = machine['prize']
        a_x, a_y = a
        b_x, b_y = b
        p_x, p_y = prize

        y = (a_y * p_x - p_y * a_x) / (b_x * a_y - b_y * a_x)
        x = (p_y - b_y * y) / a_y
        if x.is_integer() and y.is_integer():
            tokens += x * 3 + y
    print(tokens)


def part_two():
    machines = read_input()
    tokens = 0
    for machine in machines:
        a = machine['a']
        b = machine['b']
        prize = machine['prize']
        a_x, a_y = a
        b_x, b_y = b
        p_x, p_y = prize
        p_x += 10000000000000
        p_y += 10000000000000

        y = (a_y * p_x - p_y * a_x) / (b_x * a_y - b_y * a_x)
        x = (p_y - b_y * y) / a_y
        if x.is_integer() and y.is_integer():
            tokens += x * 3 + y
    print(tokens)


def read_input():
    machines = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        machine = dict()
        regex_a = r"Button A: X\+(\d+), Y\+(\d+)"
        regex_b = r"Button B: X\+(\d+), Y\+(\d+)"
        regex_prize = r"Prize: X=(\d+), Y=(\d+)"
        for line in data:
            if not line:
                machines.append(machine)
                machine = dict()
                continue

            match_a = re.match(regex_a, line)
            match_b = re.match(regex_b, line)
            match_prize = re.match(regex_prize, line)
            if match_a:
                machine['a'] = (int(match_a.group(1)), int(match_a.group(2)))
            elif match_b:
                machine['b'] = (int(match_b.group(1)), int(match_b.group(2)))
            elif match_prize:
                machine['prize'] = (int(match_prize.group(1)), int(match_prize.group(2)))

        machines.append(machine)

    return machines


if __name__ == '__main__':
    part_one()
    part_two()
