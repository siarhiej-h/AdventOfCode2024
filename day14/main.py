import re
from itertools import groupby


def part_one():
    robots = read_input()
    grid_size = (101, 103)
    for i in range(100):
        simulate_once(robots, grid_size)
    print(robots)
    q_lu, q_ru, q_ld, q_rd = calculate_quadrants(robots, grid_size)
    result = q_lu * q_ru * q_ld * q_rd
    print(result)


def simulate_once(robots, grid_size):
    for robot in robots:
        robot['position'] = (robot['position'][0] + robot['velocity'][0], robot['position'][1] + robot['velocity'][1])
        x, y = robot['position']
        if x < 0:
            x = grid_size[0] + x
        if y < 0:
            y = grid_size[1] + y
        if x >= grid_size[0]:
            x = x - grid_size[0]
        if y >= grid_size[1]:
            y = y - grid_size[1]
        robot['position'] = (x, y)


def calculate_quadrants(robots, grid_size):
    q_lu = 0
    q_ru = 0
    q_ld = 0
    q_rd = 0
    center_point = (grid_size[0] // 2, grid_size[1] // 2)
    for robot in robots:
        x, y = robot['position']
        if x < center_point[0] and y < center_point[1]:
            q_lu += 1
        elif x > center_point[0] and y < center_point[1]:
            q_ru += 1
        elif x < center_point[0] and y > center_point[1]:
            q_ld += 1
        elif x > center_point[0] and y > center_point[1]:
            q_rd += 1
    return q_lu, q_ru, q_ld, q_rd


def part_two():
    robots = read_input()
    min_safety = None
    index = None
    for i in range(1, 10403):
        simulate_once(robots, (101, 103))
        q_lu, q_ru, q_ld, q_rd = calculate_quadrants(robots, (101, 103))
        product = q_lu * q_ru * q_ld * q_rd
        if min_safety is None:
            min_safety = product

        if product < min_safety:
            min_safety = product
            index = i

    print(index)



def get_row(robots, row):
    row_robots = []
    for robot in robots:
        if robot['position'][1] == row:
            row_robots.append(robot['position'])
    return row_robots


def grid_to_string(robots, grid_size):
    grid = [['.' for _ in range(grid_size[0])] for _ in range(grid_size[1])]
    for robot in robots:
        x, y = robot['position']
        grid[y][x] = '#'
    str_repr = ''
    for row in grid:
        str_repr += ''.join(row) + '\n'
    return str_repr


def read_input():
    robots = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        regex_pattern = r"p=(-?\d+),(\d+) v=(-?\d+),(-?\d+)"
        for line in data:
            match_a = re.match(regex_pattern, line)
            position = (int(match_a.group(1)), int(match_a.group(2)))
            velocity = (int(match_a.group(3)), int(match_a.group(4)))
            robot = dict(position=position, velocity=velocity)
            robots.append(robot)

    return robots


if __name__ == '__main__':
    part_one()
    part_two()
