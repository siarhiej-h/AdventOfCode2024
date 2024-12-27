

def part_one():
    wires, gates = read_input()
    solve_all_gates(wires, gates)
    int_value = get_wire_value(wires, "z")
    print(int_value)


def get_wire_value(wires, wire_label):
    all_z_keys = [(key, value) for key, value in dict(wires.items()).items() if key.startswith(wire_label)]
    all_z_keys.sort(key=lambda x: x[0], reverse=True)
    str_value = "".join([str(1 if key[1] is True else 0) for key in all_z_keys])
    int_value = int(str_value, 2)
    return int_value


def solve_all_gates(wires, gates):
    while gates:
        changed = False
        for key, value in dict(gates.items()).items():
            left_operand, operation, right_operand = value
            if left_operand in wires and right_operand in wires:
                if operation == "AND":
                    wires[key] = wires[left_operand] & wires[right_operand]
                elif operation == "OR":
                    wires[key] = wires[left_operand] | wires[right_operand]
                elif operation == "XOR":
                    wires[key] = wires[left_operand] ^ wires[right_operand]
                gates.pop(key)
                changed = True
        if not changed:
            return False
    return True


def part_two():
    print("Do the math :shrug:")


def read_input():
    wires = dict()
    gates = dict()
    switched = False

    # ntg XOR fgs -> mjb
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            if line == "":
                switched = True
                continue

            if switched is False:
                key, value = line.split(": ")
                wires[key] = value == "1"
            else:
                parts = line.split(" ")
                left_operand = parts[0]
                operation = parts[1]
                right_operand = parts[2]
                gate = parts[4]
                gates[gate] = (left_operand, operation, right_operand)

    return wires, gates


if __name__ == '__main__':
    part_one()
    part_two()
