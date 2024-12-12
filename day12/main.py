from itertools import groupby

def part_one():
    grid = read_input()
    zones = get_all_zones(grid)
    price = sum(calculate_perimeter(zone) * len(zone) for zone in zones)
    print(price)


def get_all_zones(grid):
    visited = set()
    zone = set()
    others = set()
    grid_size = len(grid) * len(grid[0])
    populate_zone(grid, (0, 0), zone, others, visited)
    total = len(zone)
    zones = [zone]
    while total < grid_size:
        for other in list(others):
            zone = set()
            populate_zone(grid, other, zone, others, visited)
            if zone:
                zones.append(zone)
                total += len(zone)
                for pos in zone:
                    if pos in others:
                        others.remove(pos)
    return zones


def calculate_perimeter(zone):
    perimeter = 0

    for pos in zone:
        row, col = pos
        left = row - 1, col
        right = row + 1, col
        up = row, col - 1
        down = row, col + 1
        if left not in zone:
            perimeter += 1
        if right not in zone:
            perimeter += 1
        if up not in zone:
            perimeter += 1
        if down not in zone:
            perimeter += 1

    return perimeter


def calculate_sides(zone):
    sorted_rows = sorted(zone, key=lambda x: (x[0], x[1]))
    sides = 0
    for row, group in groupby(sorted_rows, key=lambda x: x[0]):
        group = list(group)
        for side in get_all_upper_sides(group, row, zone):
            sides += side
        for side in get_all_lower_sides(group, row, zone):
            sides += side

    sorted_cols = sorted(zone, key=lambda x: (x[1], x[0]))
    for col, group in groupby(sorted_cols, key=lambda x: x[1]):
        group = list(group)
        for side in get_all_left_sides(group, col, zone):
            sides += side
        for side in get_all_right_sides(group, col, zone):
            sides += side
    return sides


def get_all_upper_sides(group, row, zone):
    for i in range(0, len(group) - 1):
        this_point = group[i]
        next_point = group[i + 1]
        up = row - 1, this_point[1]

        if up not in zone and this_point[1] + 1 != next_point[1]:
            yield 1
            continue

        right_up = row - 1, this_point[1] + 1
        if up not in zone and right_up in zone:
            yield 1
            continue

    last_point = group[-1]
    up = row - 1, last_point[1]
    if up not in zone:
        yield 1


def get_all_left_sides(group, col, zone):
    for i in range(0, len(group) - 1):
        this_point = group[i]
        next_point = group[i + 1]
        left = this_point[0], col - 1

        if left not in zone and this_point[0] + 1 != next_point[0]:
            yield 1
            continue

        left_down = this_point[0] + 1, col - 1
        if left not in zone and left_down in zone:
            yield 1
            continue

    last_point = group[-1]
    left = last_point[0], col - 1
    if left not in zone:
        yield 1


def get_all_right_sides(group, col, zone):
    for i in range(0, len(group) - 1):
        this_point = group[i]
        next_point = group[i + 1]
        right = this_point[0], col + 1

        if right not in zone and this_point[0] + 1 != next_point[0]:
            yield 1
            continue

        right_down = this_point[0] + 1, col + 1
        if right not in zone and right_down in zone:
            yield 1
            continue

    last_point = group[-1]
    right = last_point[0], col + 1
    if right not in zone:
        yield 1


def get_all_lower_sides(group, row, zone):
    for i in range(0, len(group) - 1):
        this_point = group[i]
        next_point = group[i + 1]
        down = row + 1, this_point[1]

        if down not in zone and this_point[1] + 1 != next_point[1]:
            yield 1
            continue

        right_down = row + 1, this_point[1] + 1
        if down not in zone and right_down in zone:
            yield 1
            continue

    last_point = group[-1]
    down = row + 1, last_point[1]
    if down not in zone:
        yield 1


def part_two():
    stones = read_input()
    zones = get_all_zones(stones)
    total = 0
    for zone in zones:
        sides = calculate_sides(zone)
        total += sides * len(zone)
    print(total)


def populate_zone(grid, start_pos, zone, other_locations, visited):
    row, col = start_pos
    if start_pos in visited:
        return

    visited.add(start_pos)
    zone.add(start_pos)
    plant_type = grid[row][col]
    for neighbour in get_neighbors(grid, start_pos):
        if grid[neighbour[0]][neighbour[1]] == plant_type:
            populate_zone(grid, neighbour, zone, other_locations, visited)
        elif neighbour not in visited:
            other_locations.add(neighbour)


def get_neighbors(grid, pos):
    row, col = pos
    height = len(grid)
    width = len(grid[0])
    if row > 0:
        yield row - 1, col
    if row < height - 1:
        yield row + 1, col
    if col > 0:
        yield row, col - 1
    if col < width - 1:
        yield row, col + 1


def read_input():
    grid = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            grid.append(list(line))
    return grid


if __name__ == '__main__':
    part_one()
    part_two()
