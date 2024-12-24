import itertools


def part_one():
    bytes_falling = read_input()
    iterations = 1024
    grid_size = 71
    bytes_fell = simulate(bytes_falling, iterations)
    # print_fallen(bytes_fell, grid_size)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    print(find_path(start, end, grid_size, bytes_fell))


def print_fallen(bytes_fell, grid_size):
    for y in range(grid_size):
        for x in range(grid_size):
            if (x, y) in bytes_fell:
                print('#', end='')
            else:
                print('.', end='')
        print()


def find_path(start, end, grid_size, bytes_fell):
    queue = [(start, 0)]
    visited = set()
    while queue:
        position, steps = queue.pop(0)
        if position in visited:
            continue

        visited.add(position)
        for next_position in get_neighbour_positions(position, grid_size, bytes_fell):
            if next_position == end:
                return steps + 1
            else:
                queue.append((next_position, steps + 1))
    return -1


def simulate(bytes_falling, steps):
    bytes_fell = set()
    for i in range(steps):
        bytes_fell.add(bytes_falling[i])
    return bytes_fell


def get_neighbour_positions(position, grid_size, bytes_fell):
    x, y = position
    left = (x - 1, y)
    if 0 <= left[0] < grid_size and left not in bytes_fell:
        yield left

    right = (x + 1, y)
    if 0 <= right[0] < grid_size and right not in bytes_fell:
        yield right

    down = (x, y + 1)
    if 0 <= down[1] < grid_size and down not in bytes_fell:
        yield down

    up = (x, y - 1)
    if 0 <= up[1] < grid_size and up not in bytes_fell:
        yield up


def part_two():
    bytes_falling = read_input()
    grid_size = 71
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    bytes_fell = set()
    while bytes_falling:
        falling_byte = bytes_falling.pop(0)
        bytes_fell.add(falling_byte)
        steps = find_path(start, end, grid_size, bytes_fell)
        if steps == -1:
            print(falling_byte)
            break


def read_input():
    bytes_falling = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            parts = line.split(',')
            bytes_falling.append((int(parts[0]), int(parts[1])))

    return bytes_falling


if __name__ == '__main__':
    part_one()
    part_two()
