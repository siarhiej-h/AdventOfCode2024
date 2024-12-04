def part_one():
    data = read_input()
    sequence_to_find = ['X', 'M', 'A', 'S']
    all_start_positions = find_all_start_positions(data, sequence_to_find.pop(0))
    total = 0
    for start_position in all_start_positions:
        total += calculate_total_sequences(start_position, sequence_to_find.copy(), data)
    print(total)


def calculate_total_sequences(start_position, sequence_to_find, grid):
    total_found = 0
    all_directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    size_x = len(grid[0])
    size_y = len(grid)
    for direction in all_directions:
        x, y = start_position
        found = True
        for char in sequence_to_find:
            x, y = x + direction[0], y + direction[1]
            if x < 0 or x >= size_x or y < 0 or y >= size_y:
                found = False
                break
            if grid[y][x] != char:
                found = False
                break
        if found:
            total_found += 1
    return total_found


def find_all_start_positions(grid, character):
    start_positions = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == character:
                start_positions.append((x, y))

    return start_positions


def part_two():
    grid = read_input()
    all_start_positions = find_all_start_positions(grid, "A")
    total = 0
    for start_position in all_start_positions:
        if is_a_mas_cross(start_position, grid):
            total += 1
    print(total)


def is_a_mas_cross(start_position, grid):
    diagonal_coords = [
        (-1, 1),
        (1, 1),
        (1, -1),
        (-1, -1),
    ]
    chars = []
    for diagonal_coord in diagonal_coords:
        x, y = start_position[0] + diagonal_coord[0], start_position[1] + diagonal_coord[1]
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            return False
        chars.append(grid[y][x])
    string = "".join(chars)
    return string in ["MMSS", "MSSM", "SSMM", "SMMS"]


def read_input():
    grid = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            grid.append([c for c in line])

    return grid


if __name__ == '__main__':
    part_one()
    part_two()
