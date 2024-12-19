def part_one():
    grid = read_input()
    start_pos, end_pos = get_start_end_position(grid)
    start_direction = ">"
    result = find_paths(grid, start_pos, end_pos, start_direction)
    print(result)


def find_paths(grid, start_pos, end_pos, start_direction):
    visited = dict()
    min_end_score = None
    queue = [(start_pos, start_direction, 0)]
    while queue:
        position, direction, score = queue.pop(0)
        if position == end_pos:
            if min_end_score is None or score <= min_end_score:
                min_end_score = score
            continue

        if position in visited and visited[position] < score:
            continue

        visited[position] = score

        for next_position, next_score, next_direction in get_next_positions(grid, position, direction, score):
            queue.append((next_position, next_direction, next_score))
    return min_end_score


def find_paths_p2(grid, start_pos, end_pos, start_direction, target_score):
    visited = dict()
    best_tiles = set()
    queue = [(start_pos, start_direction, [], 0)]
    while queue:
        position, direction, path, score = queue.pop(0)
        if position == end_pos and score == target_score:
            for pos in path:
                best_tiles.add(pos)
            continue

        key = (position, direction)
        if key in visited and visited[key] < score:
            continue

        visited[key] = score
        path.append(position)

        for next_position, next_score, next_direction in get_next_positions(grid, position, direction, score):
            new_path = path.copy()
            queue.append((next_position, next_direction, new_path, next_score))

    return len(best_tiles) + 1


def get_next_positions(grid, position, direction, score):
    row, col = position
    height = len(grid)
    width = len(grid[0])
    left = (row, col - 1)
    if 0 <= left[0] < height and grid[left[0]][left[1]] != "#":
        new_score = score
        new_score += get_minimum_rotations(direction, "<") * 1000
        new_score += 1
        yield left, new_score, "<"

    right = (row, col + 1)
    if 0 <= right[1] < width and grid[right[0]][right[1]] != "#":
        new_score = score
        new_score += get_minimum_rotations(direction, ">") * 1000
        new_score += 1
        yield right, new_score, ">"

    up = (row - 1, col)
    if 0 <= up[0] < height and grid[up[0]][up[1]] != "#":
        new_score = score
        new_score += get_minimum_rotations(direction, "^") * 1000
        new_score += 1
        yield up, new_score, "^"

    down = (row + 1, col)
    if 0 <= down[0] < height and grid[down[0]][down[1]] != "#":
        new_score = score
        new_score += get_minimum_rotations(direction, "v") * 1000
        new_score += 1
        yield down, new_score, "v"

def get_minimum_rotations(direction, new_direction):
    directions = ['>', 'v', '<', '^']
    direction_index = directions.index(direction)
    new_direction_index = directions.index(new_direction)
    rotations_clockwise = abs(new_direction_index - direction_index)
    rotations_counter_clockwise = 4 - rotations_clockwise
    rotations = min(rotations_clockwise, rotations_counter_clockwise)
    # print(rotations)
    return rotations


def get_start_end_position(grid):
    start_pos = None
    end_pos = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                start_pos = (row, col)
            if grid[row][col] == 'E':
                end_pos = (row, col)

    return start_pos, end_pos


def part_two():
    grid = read_input()
    start_pos, end_pos = get_start_end_position(grid)
    start_direction = ">"
    target = find_paths(grid, start_pos, end_pos, start_direction)
    result = find_paths_p2(grid, start_pos, end_pos, start_direction, target)
    print(result)


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
