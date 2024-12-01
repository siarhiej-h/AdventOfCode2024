def part_one():
    left, right = read_input()
    left_sorted = sorted(left)
    right_sorted = sorted(right)
    distance = 0
    for i in range(len(left_sorted)):
        distance += abs(left_sorted[i] - right_sorted[i])
    print(distance)


def part_two():
    left, right = read_input()
    right_counts = dict()
    for number in right:
        if number in right_counts:
            right_counts[number] += 1
        else:
            right_counts[number] = 1

    total = 0
    for number in left:
        if number in right_counts:
            total += number * right_counts[number]
    print(total)


def read_input():
    left_side = []
    right_side = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            parts = line.split(' ')
            left = int(parts[0])
            right = int(parts[-1])
            left_side.append(left)
            right_side.append(right)
    return left_side, right_side


if __name__ == '__main__':
    part_one()
    part_two()