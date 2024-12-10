from collections import defaultdict
from itertools import combinations

def part_one():
    grid = read_input()
    antenna_coordinates = get_antennas(grid)

    grid_height = len(grid)
    grid_width = len(grid[0])
    unique_locations = set()
    for frequency, coordinates in antenna_coordinates.items():
        for left, right in combinations(coordinates, 2):
            left_column, left_row = left
            right_column, right_row = right
            x_diff = right_column - left_column
            y_diff = right_row - left_row
            first_antinode = (left_column - x_diff, left_row - y_diff)
            second_antinode = (right_column + x_diff, right_row + y_diff)
            if 0 <= first_antinode[0] < grid_height and 0 <= first_antinode[1] < grid_width:
                unique_locations.add(first_antinode)
            if 0 <= second_antinode[0] < grid_height and 0 <= second_antinode[1] < grid_width:
                unique_locations.add(second_antinode)
    print(len(unique_locations))


def get_antennas(grid):
    antenna_coordinates = defaultdict(list)
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row] != '.':
                antenna_frequency = grid[column][row]
                antenna_coordinates[antenna_frequency].append((column, row))
    return antenna_coordinates


def part_two():
    grid = read_input()
    antenna_coordinates = get_antennas(grid)

    grid_height = len(grid)
    grid_width = len(grid[0])
    unique_locations = set()
    for frequency, coordinates in antenna_coordinates.items():
        for left, right in combinations(coordinates, 2):
            unique_locations.add(left)
            unique_locations.add(right)

            left_column, left_row = left
            right_column, right_row = right
            x_diff = right_column - left_column
            y_diff = right_row - left_row

            multiplier = 1
            while True:
                first_antinode = (left_column - x_diff * multiplier, left_row - y_diff * multiplier)
                if 0 <= first_antinode[0] < grid_height and 0 <= first_antinode[1] < grid_width:
                    unique_locations.add(first_antinode)
                    multiplier += 1
                else:
                    break

            multiplier = 1
            while True:
                second_antinode = (right_column + x_diff * multiplier, right_row + y_diff * multiplier)
                if 0 <= second_antinode[0] < grid_height and 0 <= second_antinode[1] < grid_width:
                    unique_locations.add(second_antinode)
                    multiplier += 1
                else:
                    break
    print(len(unique_locations))


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
