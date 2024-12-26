import itertools
import math


def part_one():
    codes = read_input()
    for i in range(0, 2000):
        for j in range(len(codes)):
            codes[j] = simulate_once(codes[j])
    total = sum(codes)
    print(total)


def part_two():
    codes = read_input()

    banana_maps = []
    all_sequences = set()
    for code in codes:
        banana_map = dict()
        previous_price = code % 10
        code = simulate_once(code)
        price_1 = code % 10
        diff_1 = price_1 - previous_price

        code = simulate_once(code)
        price_2 = code % 10
        diff_2 = price_2 - price_1

        code = simulate_once(code)
        price_3 = code % 10
        diff_3 = price_3 - price_2

        code = simulate_once(code)
        price_4 = code % 10
        diff_4 = price_4 - price_3
        sequence = (diff_1, diff_2, diff_3, diff_4)
        banana_map[sequence] = price_4
        for i in range(0, 1996):
            price_3, price_2, price_1, previous_price = price_4, price_3, price_2, price_1
            code = simulate_once(code)
            price_4 = code % 10
            diff_3, diff_2, diff_1 = diff_4, diff_3, diff_2
            diff_4 = price_4 - price_3
            sequence = (diff_1, diff_2, diff_3, diff_4)
            if sequence not in banana_map:
                banana_map[sequence] = price_4
        banana_maps.append(banana_map)
        all_sequences.update(banana_map.keys())

    max_bananas = 0
    for sequence in all_sequences:
        bananas_per_sequence = 0
        for banana_map in banana_maps:
            if sequence in banana_map:
                bananas_per_sequence += banana_map[sequence]
        max_bananas = max(max_bananas, bananas_per_sequence)
    print(max_bananas)


def simulate_once(secret_number):
    first_step = prune(mix(secret_number * 64, secret_number))
    second_step = prune(mix(math.floor(first_step / 32), first_step))
    third_step = prune(mix(second_step * 2048, second_step))
    return third_step


def prune(secret_number):
    return secret_number % 16777216


def mix(number, secret_number):
    return number ^ secret_number


def read_input():
    initial_numbers = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            initial_numbers.append(int(line))

    return initial_numbers


if __name__ == '__main__':
    part_one()
    part_two()
