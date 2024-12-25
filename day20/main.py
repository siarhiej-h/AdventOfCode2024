from collections import defaultdict


def part_one():
    grid = read_input()
    start, end = find_start_end(grid)
    all_positions = {(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == '.'}
    path = find_path(all_positions, start, end)
    cheats = find_cheats(path, 100, 2)
    total = sum(cheats.values())
    print(total)


def find_path(all_positions, start, end):
    path = [start]
    previous = None
    while True:
        current = path[-1]
        for diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_position = (current[0] + diff[0], current[1] + diff[1])
            if next_position == end:
                path.append(next_position)
                return path

            if next_position in all_positions and next_position != previous:
                path.append(next_position)
                previous = current
                break


def find_cheats(path, min_reduction, max_cheat_duration):
    cheats = defaultdict(int)
    distances = {position: i for i, position in enumerate(path)}
    for i in range(len(path)):
        position = path[i]
        for j in range(-max_cheat_duration, max_cheat_duration + 1):
            for k in range(-max_cheat_duration, max_cheat_duration + 1):
                cheat_duration = abs(j) + abs(k)
                next_position = (position[0] + j, position[1] + k)
                if cheat_duration > max_cheat_duration or cheat_duration == 0:
                    continue

                if next_position in distances:
                    new_distance = distances[position] + cheat_duration
                    reduction = distances[next_position] - new_distance
                    if reduction >= min_reduction:
                        cheats[reduction] += 1
    return cheats


def part_two():
    grid = read_input()
    start, end = find_start_end(grid)
    all_positions = {(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == '.'}
    path = find_path(all_positions, start, end)
    cheats = find_cheats(path, 100, 20)
    total = sum(cheats.values())
    print(total)


def find_start_end(grid):
    start = None
    end = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'E':
                end = (i, j)
            if start is not None and end is not None:
                break

    return start, end


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
