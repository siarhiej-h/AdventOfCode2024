def part_one():
    grid, moves = read_input()
    start_pos = get_start_position(grid)
    pos = start_pos
    for move in moves:
        pos = move_robot(grid, pos, move)

    total_gps = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                total_gps += gps((row, col))

    print(total_gps)

    # grid_str = "".join(["".join(row) + "\n" for row in grid])


def get_start_position(grid):
    start_pos = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                start_pos = (row, col)
                break
    return start_pos


def gps(pos):
    row, col = pos
    return 100 * row + col



def move_robot(grid, pos, direction):
    row, col = pos
    new_row, new_col = row, col
    if direction == ">":
        new_col += 1
    elif direction == "<":
        new_col -= 1
    elif direction == "^":
        new_row -= 1
    elif direction == "v":
        new_row += 1

    if grid[new_row][new_col] == "#":
        return row, col

    if grid[new_row][new_col] == "O":
        if try_move_box(grid, (new_row, new_col), direction):
            grid[row][col] = "."
            grid[new_row][new_col] = "@"
            return new_row, new_col

    if grid[new_row][new_col] == ".":
        grid[row][col] = "."
        grid[new_row][new_col] = "@"
        return new_row, new_col

    return row, col


def try_move_box(grid, pos, direction):
    row, col = pos
    new_row, new_col = row, col
    if direction == ">":
        new_col += 1
    elif direction == "<":
        new_col -= 1
    elif direction == "^":
        new_row -= 1
    elif direction == "v":
        new_row += 1

    if grid[new_row][new_col] == "#":
        return False

    if grid[new_row][new_col] == "O":
        has_box_moved = try_move_box(grid, (new_row, new_col), direction)
        if has_box_moved:
            grid[new_row][new_col] = "O"
            grid[row][col] = "."
            return True

    if grid[new_row][new_col] == ".":
        grid[new_row][new_col] = "O"
        grid[row][col] = "."
        return True

    return False


def part_two():
    grid, moves = read_input()
    updated_grid = []
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                new_row.extend("[]")
            elif grid[row][col] == "@":
                new_row.extend("@.")
            elif grid[row][col] == "#":
                new_row.extend("##")
            else:
                new_row.extend("..")
        updated_grid.append(new_row)

    grid = updated_grid
    grid_str = "".join(["".join(row) + "\n" for row in grid])
    # print(grid_str)
    # print_robot_area(grid)

    start_pos = get_start_position(grid)
    for move in moves:
        # print(move)
        start_pos = move_robot_p2(grid, start_pos, move)
        # print_robot_area(grid)
        # grid_str = "".join(["".join(row) + "\n" for row in grid])
        # print(grid_str)

    total_gps = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "[":
                total_gps += gps((row, col))

    print(total_gps)


def print_robot_area(grid):
    position = get_start_position(grid)
    row, col = position
    str_result = ""
    size_up = 5
    if row < 5:
        size_up = row
    size_down = 5
    if row + 5 >= len(grid):
        size_down = len(grid) - row - 1
    size_left = 5
    if col < 5:
        size_left = col
    size_right = 5
    if col + 5 >= len(grid[0]):
        size_right = len(grid[0]) - col - 1
    for i in range(row - size_up, row + size_down + 1):
        for j in range(col - size_left, col + size_right + 1):
            if i == row and j == col:
                str_result += "@"
            else:
                str_result += grid[i][j]
        str_result += "\n"
    print(str_result)


def move_robot_p2(grid, pos, direction):
    row, col = pos
    new_row, new_col = row, col
    if direction == ">":
        new_col += 1
    elif direction == "<":
        new_col -= 1
    elif direction == "^":
        new_row -= 1
    elif direction == "v":
        new_row += 1

    if grid[new_row][new_col] == "#":
        return row, col

    if grid[new_row][new_col] == ".":
        grid[row][col] = "."
        grid[new_row][new_col] = "@"
        return new_row, new_col

    if grid[new_row][new_col] in ["[", "]"]:
        box = grid[new_row][new_col]
        if box == "[":
            left_col, right_col = new_col, new_col + 1
        else:
            left_col, right_col = new_col - 1, new_col

        boxes_to_move = [(new_row, left_col, right_col)]
        if try_move_boxes_p2(grid, boxes_to_move, direction):
            grid[row][col] = "."
            grid[new_row][new_col] = "@"
            return new_row, new_col

    return row, col


def try_move_boxes_p2(grid, boxes, direction):
    new_boxes = []
    for box in boxes:
        row, left_col, right_col = box
        if direction == ">":
            left_col += 1
            right_col += 1
        elif direction == "<":
            left_col -= 1
            right_col -= 1
        elif direction == "^":
            row -= 1
        elif direction == "v":
            row += 1
        new_boxes.append((row, left_col, right_col))

    boxes_to_move = set()
    for box in new_boxes:
        new_row, new_left_col, new_right_col = box
        if grid[new_row][new_left_col] == "#" or grid[new_row][new_right_col] == "#":
            return False

        if direction in ["^", "v"]:
            if grid[new_row][new_left_col] in ["[", "]"] or grid[new_row][new_right_col] in ["[", "]"]:
                if grid[new_row][new_left_col] == "]":
                    boxes_to_move.add((new_row, new_left_col - 1, new_left_col))
                if grid[new_row][new_right_col] == "[":
                    boxes_to_move.add((new_row, new_right_col, new_right_col + 1))
                if grid[new_row][new_left_col] == "[" and grid[new_row][new_right_col] == "]":
                    boxes_to_move.add((new_row, new_left_col, new_right_col))
        elif direction == ">":
            if grid[new_row][new_right_col] == "[":
                boxes_to_move.add((new_row, new_right_col, new_right_col + 1))
        elif direction == "<":
            if grid[new_row][new_left_col] == "]":
                boxes_to_move.add((new_row, new_left_col - 1, new_left_col))

    if boxes_to_move:
        all_can_move = try_move_boxes_p2(grid, list(boxes_to_move), direction)
        if all_can_move:
            for box in boxes:
                row, left_col, right_col = box
                grid[row][left_col] = "."
                grid[row][right_col] = "."
            for box in new_boxes:
                row, left_col, right_col = box
                grid[row][left_col] = "["
                grid[row][right_col] = "]"
            return True
        return False

    if direction == "<":
        box = new_boxes[0]
        row, left_col, right_col = box
        if grid[row][left_col] == ".":
            grid[row][left_col] = "["
            grid[row][right_col] = "]"
            grid[row][right_col + 1] = "."
            return True
        return False

    if direction == ">":
        box = new_boxes[0]
        row, left_col, right_col = box
        if grid[row][right_col] == ".":
            grid[row][left_col] = "["
            grid[row][right_col] = "]"
            grid[row][left_col - 1] = "."
            return True
        return False

    if all(grid[row][left_col] == "." and grid[row][right_col] == "." for row, left_col, right_col in new_boxes):
        for box in boxes:
            row, left_col, right_col = box
            grid[row][left_col] = "."
            grid[row][right_col] = "."
        for box in new_boxes:
            row, left_col, right_col = box
            grid[row][left_col] = "["
            grid[row][right_col] = "]"
        return True

    return False


def read_input():
    grid = []
    moves = []
    next_part = False
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()

        for line in data:
            if not line:
                next_part = True
                continue

            if next_part:
                moves += list(line)
            else:
                grid.append(list(line))

    return grid, moves


if __name__ == '__main__':
    part_one()
    part_two()
