def part_one():
    lines = read_input()
    total_safe = sum([is_safe(levels) for levels in lines])
    print(total_safe)

def check_adjacent_levels(levels):
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff > 3 or diff == 0:
            return False
    return True


def is_safe(levels):
    sorted_levels = sorted(levels)
    if sorted_levels == levels:
        return check_adjacent_levels(levels)

    if sorted_levels == levels[::-1]:
        levels = levels[::-1]
        return check_adjacent_levels(levels)

    return False


def is_safe_allowing_one_removal(levels):
    is_report_safe = is_safe(levels)
    if is_report_safe is True:
        return True

    for k in range(0, len(levels)):
        levels_copy = levels.copy()
        levels_copy.pop(k)
        is_report_safe = is_safe(levels_copy)
        if is_report_safe:
            return True

    return is_report_safe


def part_two():
    lines = read_input()
    total_safe = sum([is_safe_allowing_one_removal(levels) for levels in lines])
    print(total_safe)


def read_input():
    lines = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            levels = [int(l) for l in line.split(" ")]
            lines.append(levels)

    return lines


if __name__ == '__main__':
    part_one()
    part_two()