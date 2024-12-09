def part_one():
    grid = read_input()
    direction, start_pos = get_start_position(grid)
    current_position = start_pos
    stepped_outside = False
    positions = {current_position}
    while stepped_outside is False:
        stepped_outside = stepping_outside(grid, current_position, direction)
        if stepped_outside:
            break
        if can_move(grid, current_position, direction):
            current_position = move(current_position, direction)
            positions.add(current_position)
        else:
            direction = turn_right(direction)

    print(len(positions))


def get_start_position(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] in ['^', 'v', '<', '>']:
                start_pos = (row, col)
                direction = grid[row][col]
                return direction, start_pos
    return None


def stepping_outside(grid, pos, direction):
    row, col = pos
    if direction == '^':
        return row == 0
    elif direction == 'v':
        return row == len(grid) - 1
    elif direction == '<':
        return col == 0
    elif direction == '>':
        return col == len(grid[0]) - 1


def move(pos, direction):
    row, col = pos
    if direction == '^':
        return row - 1, col
    elif direction == 'v':
        return row + 1, col
    elif direction == '<':
        return row, col - 1
    elif direction == '>':
        return row, col + 1


def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'
    elif direction == '>':
        return 'v'


def can_move(grid, pos, direction):
    row, col = pos
    if direction == '^':
        return grid[row - 1][col] != '#'
    elif direction == 'v':
        return grid[row + 1][col] != '#'
    elif direction == '<':
        return grid[row][col - 1] != '#'
    elif direction == '>':
        return grid[row][col + 1] != '#'


def part_two():
    grid = read_input()
    direction, start_pos = get_start_position(grid)
    loops_possible = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#' or (i, j) == start_pos:
                continue
            grid[i][j] = '#'
            if is_loop(grid, start_pos, direction):
                loops_possible += 1
            grid[i][j] = '.'
    print(loops_possible)


def is_loop(grid, start_pos, direction):
    current_row, current_col = start_pos
    positions = {(current_row, current_col, direction)}
    while True:
        stepped_outside = stepping_outside(grid, (current_row, current_col), direction)
        if stepped_outside:
            return False
        if can_move(grid, (current_row, current_col), direction):
            current_row, current_col = move((current_row, current_col), direction)
            if (current_row, current_col, direction) in positions:
                return True
            positions.add((current_row, current_col, direction))
        else:
            direction = turn_right(direction)


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
