import functools
from collections import defaultdict

num_pad = [['7','8','9'], ['4','5','6'], ['1','2','3'], [None, '0', 'A']]
directional_pad = [[None, '^', 'A'], ['<', 'v', '>']]


def get_all_pairs(pad):
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            for k in range(len(pad)):
                for l in range(len(pad[k])):
                    start = pad[i][j]
                    end = pad[k][l]
                    if start is None or end is None:
                        continue
                    yield start, end


def is_path_zig_zag(path):
    all_characters = defaultdict(list)
    for index, character in enumerate(path):
        all_characters[character].append(index)

    if len(all_characters) == 1:
        return False

    for indexes in all_characters.values():
        for m in range(1, len(indexes)):
            if abs(indexes[m] - indexes[m - 1]) > 1:
                return True
    return False


def find_position(grid, code):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == code:
                return i, j


def find_shortest_path(grid, start, target):
    start_position = find_position(grid, start)
    visited = set()
    grid_height = len(grid)
    grid_width = len(grid[0])
    queue = [(start_position, [])]
    while queue:
        current_position, path = queue.pop(0)
        if current_position in visited:
            continue

        value = grid[current_position[0]][current_position[1]]
        if value == target:
            return path

        visited.add(current_position)
        for diff in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_pos = (current_position[0] + diff[0], current_position[1] + diff[1])
            if new_pos[0] < 0 or new_pos[0] >= grid_height or new_pos[1] < 0 or new_pos[1] >= grid_width:
                continue
            if grid[new_pos[0]][new_pos[1]] is None:
                continue
            new_path = path.copy()
            new_path.append(translate_direction(diff))
            queue.append((new_pos, new_path))


def find_all_shortest_paths(grid, start, target):
    shortest_path = find_shortest_path(grid, start, target)
    path_length = len(shortest_path)
    all_paths = list(find_all_paths(grid, start, target, path_length))
    return all_paths


def find_all_paths(grid, start, target, path_length):
    start_position = find_position(grid, start)
    grid_height = len(grid)
    grid_width = len(grid[0])
    queue = [(start_position, [])]
    while queue:
        current_position, path = queue.pop(0)
        value = grid[current_position[0]][current_position[1]]
        if value == target:
            yield path

        if len(path) == path_length:
            continue

        for diff in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_pos = (current_position[0] + diff[0], current_position[1] + diff[1])
            if new_pos[0] < 0 or new_pos[0] >= grid_height or new_pos[1] < 0 or new_pos[1] >= grid_width:
                continue
            if grid[new_pos[0]][new_pos[1]] is None:
                continue
            new_path = path.copy()
            new_path.append(translate_direction(diff))
            queue.append((new_pos, new_path))


def translate_direction(diff):
    if diff == (0, 1):
        return '>'
    elif diff == (0, -1):
        return '<'
    elif diff == (1, 0):
        return 'v'
    elif diff == (-1, 0):
        return '^'


def calculate_all_sequences(pad):
    sequences = dict()
    for start, end in get_all_pairs(pad):
        if (start, end) in sequences:
            continue

        all_shortest = find_all_shortest_paths(pad, start, end)
        all_shortest_strings = []
        for paths in all_shortest:
            if is_path_zig_zag(paths) is False:
                all_shortest_strings.append(''.join(paths) + 'A')

        sequences[(start, end)] = all_shortest_strings
    return sequences


all_num_sequences = calculate_all_sequences(num_pad)
all_directional_sequences = calculate_all_sequences(directional_pad)


def get_code_segment_options(code, is_num_pad):
    start_code = 'A'
    paths_map = all_num_sequences if is_num_pad else all_directional_sequences
    for c in code:
        paths = paths_map[(start_code, c)]
        yield paths
        start_code = c


@functools.cache
def get_min_length(code, depth):
    if depth == 0:
        return len(code)

    total = 0
    for segment_options in get_code_segment_options(code, False):
        min_length = None
        for segment in segment_options:
            length = get_min_length(segment, depth - 1)
            if min_length is None or length < min_length:
                min_length = length
        total += min_length
    return total


def part_one():
    codes = read_input()
    total = 0
    for code in codes:
        code_total = sum(
            min(get_min_length(option, 2) for option in segment_options)
            for segment_options in get_code_segment_options(code, True)
        )
        int_part = int(code[:-1])
        total += code_total * int_part
    print(total)


def part_two():
    codes = read_input()
    total = 0
    for code in codes:
        code_total = sum(
            min(get_min_length(option, 25) for option in segment_options)
            for segment_options in get_code_segment_options(code, True)
        )
        int_part = int(code[:-1])
        total += code_total * int_part
    print(total)


def read_input():
    codes = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            codes.append(line)

    return codes


if __name__ == '__main__':
    part_one()
    part_two()
