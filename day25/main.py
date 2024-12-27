import itertools


def part_one():
    keys, locks = read_input()
    total = sum(1 for key in keys for lock in locks if is_key_for_lock(key, lock))
    print(total)


def is_key_for_lock(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
    return True


def read_input():
    shapes = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        shape = []
        for line in data:
            if line == '':
                shapes.append(shape)
                shape = []
            else:
                shape.append(line)
        shapes.append(shape)
    return get_locks_and_keys(shapes)


def get_locks_and_keys(shapes):
    locks = []
    keys = []
    for shape in shapes:
        if all(ch == "#" for ch in shape[0]):
            lock = transform_shape(shape, range(1, len(shape)))
            locks.append(lock)
        else:
            key = transform_shape(shape, range(len(shape) - 2, 0, -1))
            keys.append(key)
    return keys, locks


def transform_shape(shape, rows):
    transformed = [
        sum(1 for _ in itertools.takewhile(lambda row: shape[row][col] == '#', rows))
        for col in range(len(shape[0]))
    ]
    return transformed


if __name__ == '__main__':
    part_one()
