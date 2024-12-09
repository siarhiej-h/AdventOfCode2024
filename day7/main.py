from itertools import product

def part_one():
    data = read_input()
    total = 0
    for test_value, arguments in data:
        all_operator_combinations = product(["+", "*"], repeat=len(arguments) - 1)
        for operators in all_operator_combinations:
            if evaluate_expression(test_value, arguments, operators):
                total += test_value
                break
    print(total)


def evaluate_expression(test_value, arguments, operators):
    first_argument = arguments[0]
    for i in range(1, len(arguments)):
        second_argument = arguments[i]
        operator = operators[i - 1]
        if operator == "+":
            first_argument += second_argument
        elif operator == "*":
            first_argument *= second_argument
        elif operator == "|":
            first_argument = int(str(first_argument) + str(second_argument))
    return first_argument == test_value


def part_two():
    data = read_input()
    total = 0
    for test_value, arguments in data:
        all_operator_combinations = product(["+", "*", "|"], repeat=len(arguments) - 1)
        for operators in all_operator_combinations:
            if evaluate_expression(test_value, arguments, operators):
                total += test_value
                break
    print(total)


def read_input():
    lines = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            parts = line.split(": ")
            test_value = int(parts[0])
            arguments = [int(arg) for arg in parts[1].split(" ")]
            lines.append((test_value, arguments))
    return lines


if __name__ == '__main__':
    part_one()
    part_two()
