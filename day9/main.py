from itertools import count


def part_one():
    digits = read_input()

    total = 0
    stream_value = ""
    for position, file_id in read_converted_stream(digits):
        total += position * file_id
        stream_value += str(file_id)

    # print(stream_value)
    print(total)


def read_file_bits_from_end(digits):
    file_id = len(digits) // 2
    for digit in reversed(digits[::2]):
        for i in range(0, int(digit)):
            yield file_id
        file_id -= 1


def read_converted_stream(digits):
    ends_with_spaces = len(digits) % 2 == 0
    if ends_with_spaces:
        digits.pop(-1)

    spaces = False
    position = 0
    file_id = 0

    total_file_blocks = sum(int(digit) for digit in digits[::2])
    digits_from_end_generator = read_file_bits_from_end(digits)
    for digit in digits:
        if spaces is False:
            for i in range(0, int(digit)):
                yield position, file_id
                position += 1
                if position == total_file_blocks:
                    return
        else:
            file_id += 1
            for i in range(0, int(digit)):
                yield position, next(digits_from_end_generator)
                position += 1

        spaces = not spaces


def read_files_from_end(digits):
    file_id = len(digits) // 2
    for digit in reversed(digits[::2]):
        yield file_id, int(digit)
        file_id -= 1


def move_entire_files_read_converted_stream(digits):
    ends_with_spaces = len(digits) % 2 == 0
    if ends_with_spaces:
        digits.pop(-1)

    file_system = []
    spaces = False
    file_id = 0
    for digit in digits:
        size = int(digit)
        if spaces is False:
            file_system.append((file_id, size))
        else:
            file_id += 1
            if size > 0:
                file_system.append((None, size))
        spaces = not spaces

    files = [(file_id, size) for file_id, size in reversed(file_system) if file_id is not None]
    for file_id, size in files:
        file_index = next(i for i, (f_id, s) in enumerate(file_system) if f_id == file_id)
        gap_index = next((i for i, (file_id, gap_size) in enumerate(file_system) if file_id is None and gap_size >= size and i < file_index), None)
        if gap_index is not None:
            move_file_into_a_gap(file_id, size, file_system, gap_index)

    position = 0
    for file_id, size in file_system:
        if file_id is not None:
            for i in range(0, size):
                yield position, file_id
                position += 1
        else:
            position += size

    return file_system


def move_file_into_a_gap(file_id, size, file_system, gap_index):
    index = next(i for i, (f_id, size) in enumerate(file_system) if f_id == file_id)
    file = file_system.pop(index)
    file_system.insert(index, (None, size))
    gap = file_system.pop(gap_index)
    file_system.insert(gap_index, file)
    if gap[1] > size:
        new_gap = (None, gap[1] - size)
        file_system.insert(gap_index + 1, new_gap)


def part_two():
    digits = read_input()

    total = 0
    stream_value = ""
    converted_file_system = move_entire_files_read_converted_stream(digits)
    for position, file_id in converted_file_system:
        total += position * file_id
        # stream_value += str(file_id)

    # print(stream_value)
    print(total)


def read_input():
    with open('input.txt', 'r') as file:
        data = file.read()
    return list(data)


if __name__ == '__main__':
    part_one()
    part_two()
