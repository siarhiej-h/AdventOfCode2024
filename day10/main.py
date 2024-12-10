from collections import defaultdict
from itertools import combinations

def part_one():
    grid = read_input()
    all_starting_positions = get_all_starting_positions(grid, 0)

    total = 0
    for start_position in all_starting_positions:
        target_positions = set()
        find_all_paths(grid, start_position, 9, target_positions)
        total += len(target_positions)

    print(total)


def get_all_starting_positions(grid, value):
    positions = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == value:
                positions.append((row, col))
    return positions


def get_neighbors(grid, position):
    row, col = position
    rows = len(grid)
    cols = len(grid[0])
    value = grid[row][col]
    if row > 0 and grid[row - 1][col] == value + 1:
        yield row - 1, col
    if row < rows - 1 and grid[row + 1][col] == value + 1:
        yield row + 1, col
    if col > 0 and grid[row][col - 1] == value + 1:
        yield row, col - 1
    if col < cols - 1 and grid[row][col + 1] == value + 1:
        yield row, col + 1


def find_all_paths(grid, start_position, target, target_positions):
    row, col = start_position
    if target == grid[row][col]:
        target_positions.add(start_position)
        return

    for neighbor in get_neighbors(grid, start_position):
        find_all_paths(grid, neighbor, target, target_positions)


def part_two():
    grid = read_input()
    all_starting_positions = get_all_starting_positions(grid, 0)

    total = 0
    for start_position in all_starting_positions:
        total += find_all_paths_p2(grid, start_position, 9, 0)

    print(total)


def find_all_paths_p2(grid, start_position, target, total):
    row, col = start_position
    if target == grid[row][col]:
        return total + 1

    for neighbor in get_neighbors(grid, start_position):
        total = find_all_paths_p2(grid, neighbor, target, total)

    return total


def read_input():
    grid = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            grid.append(list((int(d) for d in line)))
    return grid


if __name__ == '__main__':
    part_one()
    part_two()
