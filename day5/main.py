from collections import defaultdict


def part_one():
    rules, updates = read_input()
    graph = defaultdict(set)
    for rule in rules:
        graph[rule[0]].add(rule[1])

    total_middle = 0
    for update_line in updates:
        is_correct_order, _ = is_line_in_order(graph, update_line)
        if is_correct_order:
            total_middle += update_line[len(update_line) // 2]

    print(total_middle)


def is_line_in_order(graph, update_line):
    for i in range(0, len(update_line) - 1):
        if update_line[i] in graph[update_line[i + 1]]:
            return False, i
    return True, None


def part_two():
    rules, updates = read_input()
    graph = defaultdict(set)
    for rule in rules:
        graph[rule[0]].add(rule[1])

    total_middle = 0
    for update_line in updates:
        is_correct_order, index = is_line_in_order(graph, update_line)
        if not is_correct_order:
            while not is_correct_order:
                left, right = update_line[index], update_line[index + 1]
                update_line[index], update_line[index + 1] = right, left
                is_correct_order, index = is_line_in_order(graph, update_line)
            total_middle += update_line[len(update_line) // 2]

    print(total_middle)


def read_input():
    order_rules = []
    updates = []
    rule2 = False
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            if not line:
                rule2 = True
                continue
            if not rule2:
                order_rules.append([int(n) for n in line.split('|')])
            else:
                updates.append([int(n) for n in line.split(',')])

    return order_rules, updates


if __name__ == '__main__':
    part_one()
    part_two()
