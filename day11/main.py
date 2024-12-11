from collections import defaultdict

def part_one():
    stones = read_input()
    evolve(stones, 25)
    total = sum(count for stone, count in stones.items())
    print(total)


def evolve(stones, number_of_blinks):
    for _ in range(number_of_blinks):
        evolve_once(stones)
    return stones


def evolve_once(stones):
    for stone, count in dict(stones).items():
        if stone == 0:
            stones[1] += count
            stones[stone] -= count
            continue

        str_stone = str(stone)
        stone_length = len(str_stone)
        if stone_length % 2 == 0:
            left_stone = int(str_stone[:stone_length // 2])
            right_stone = int(str_stone[stone_length // 2:])
            stones[left_stone] += count
            stones[right_stone] += count
            stones[stone] -= count
            continue

        stones[stone * 2024] += count
        stones[stone] -= count


def part_two():
    stones = read_input()
    evolve(stones, 75)
    total = sum(count for stone, count in stones.items())
    print(total)


def read_input():
    with open('input.txt', 'r') as file:
        data = file.read()
        stones = defaultdict(int)
        for s in data.split(" "):
            stones[int(s)] += 1
        return stones


if __name__ == '__main__':
    part_one()
    part_two()
