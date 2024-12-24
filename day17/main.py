import itertools
import re


def part_one():
    registers, program = read_input()
    printed = process_all_instructions(registers, program)

    print(",".join([str(x) for x in printed]))


def get_operand_combo_value(operand, registers):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers['A']
    if operand == 5:
        return registers['B']
    if operand == 6:
        return registers['C']
    if operand == 7:
        raise ValueError("Invalid operand value")


def process_instruction(instruction, operand, registers, index, printed):
    if instruction == 0:
        denominator = 2 ** get_operand_combo_value(operand, registers)
        registers['A'] //= denominator
    elif instruction == 1:
        registers['B'] ^= operand
    elif instruction == 2:
        registers['B'] = get_operand_combo_value(operand, registers) % 8
    elif instruction == 3:
        if registers['A'] != 0:
            return operand
    elif instruction == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif instruction == 5:
        value = get_operand_combo_value(operand, registers) % 8
        printed.append(value)
    elif instruction == 6:
        denominator = 2 ** get_operand_combo_value(operand, registers)
        registers['B'] = registers['A'] // denominator
    elif instruction == 7:
        denominator = 2 ** get_operand_combo_value(operand, registers)
        registers['C'] = registers['A'] // denominator
    return index + 2


def part_two():
    registers, program = read_input()
    start_values = ['1'] + ['0'] * 15
    offset = 0
    while offset < 16:
        oct_value = f"0o{"".join(start_values)}"
        a_value = int(oct_value, 8)
        registers_copy = registers.copy()
        registers_copy['A'] = a_value
        printed = process_all_instructions(registers_copy, program)
        while printed[-1 - offset] != program[-1 - offset]:
            value = int(start_values[offset])
            if value == 7:
                start_values[offset] = '0'
                offset -= 1
                printed = shift_forward(offset, program, registers.copy(), start_values, start_values[offset])
                continue

            printed = shift_forward(offset, program, registers.copy(), start_values, value)

        offset += 1

    oct_value = f"0o{"".join(start_values)}"
    a_value = int(oct_value, 8)
    print(a_value)


def shift_forward(offset, program, registers, start_values, value):
    start_values[offset] = str(int(value) + 1)
    oct_value = f"0o{"".join(start_values)}"
    a_value = int(oct_value, 8)
    registers['A'] = a_value
    return process_all_instructions(registers, program)


def process_all_instructions(registers, program):
    index = 0
    printed = []
    while index < len(program):
        instruction = program[index]
        operand = program[index + 1]
        index = process_instruction(instruction, operand, registers, index, printed)
    return printed


def read_input():
    registers = dict()
    program = []
    register_regex_pattern = r'^Register (?P<name>[A-Z]): (?P<value>\d+)$'
    program_regex_pattern = "\\d"
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            if re.match(register_regex_pattern, line):
                match = re.match(register_regex_pattern, line)
                registers[match.group('name')] = int(match.group('value'))
            if "Program" in line:
                for match in re.findall(program_regex_pattern, line):
                    program.append(int(match))

    return registers, program


if __name__ == '__main__':
    part_one()
    part_two()
