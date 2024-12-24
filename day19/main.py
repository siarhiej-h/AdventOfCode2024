import itertools


def part_one():
    towels, designs = read_input()
    total = 0
    known_designs = dict()
    for design in designs:
        if is_design_possible(towels, design, known_designs):
            total += 1

    print(total)


def is_design_possible(towels, design, known_designs):
    if design in known_designs:
        return known_designs[design]

    while design:
        designs_to_check = []
        for towel in towels:
            if design.startswith(towel):
                designs_to_check.append(design[len(towel):])

        if not designs_to_check:
            known_designs[design] = False
            return False


        for new_design in designs_to_check:
            if new_design == '':
                known_designs[design] = True
                return True

            if is_design_possible(towels, new_design, known_designs):
                known_designs[design] = True
                return True
        else:
            known_designs[design] = False
            return False

    return True


def get_total_design_count(towels, design, known_designs):
    if design in known_designs:
        return known_designs[design]

    if design == '':
        return 1

    total = 0
    designs_to_check = []
    for towel in towels:
        if design.startswith(towel):
            designs_to_check.append(design[len(towel):])

    if not designs_to_check:
        known_designs[design] = 0
        return 0

    for new_design in designs_to_check:
        possible_design_combos = get_total_design_count(towels, new_design, known_designs)
        total += possible_design_combos

    known_designs[design] = total
    return total


def part_two():
    towels, designs = read_input()
    total = 0
    known_designs = dict()
    for design in designs:
        total += get_total_design_count(towels, design, known_designs)

    print(total)


def read_input():
    towels_read = False
    designs = []
    towels = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            if line == '':
                towels_read = True
                continue

            if not towels_read:
                towels += line.split(", ")
            else:
                designs.append(line)

    return towels, designs


if __name__ == '__main__':
    part_one()
    part_two()
