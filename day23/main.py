import itertools


def part_one():
    links = read_input()
    nodes = organize_nodes(links)
    get_all_three_sets(nodes)


def organize_nodes(links):
    nodes = {}
    for left, right in links:
        if left not in nodes:
            nodes[left] = Node(left)
        if right not in nodes:
            nodes[right] = Node(right)
        nodes[left].add_connection(right)
        nodes[right].add_connection(left)
    return nodes


def get_all_three_sets(nodes):
    unique_triangles = set()
    for node in nodes.values():
        name = node.name
        node_connections = list(node.connections)
        for i in range(0, len(node.connections)):
            node_i = nodes[node_connections[i]]
            node_i_name = node_i.name
            for j in range(i + 1, len(node.connections)):
                node_j_name = node_connections[j]
                if node_j_name in node_i.connections:
                    if name.startswith("t") or node_i_name.startswith("t") or node_j_name.startswith("t"):
                        triangle = [name, node_i_name, node_j_name]
                        triangle.sort()
                        unique_triangles.add(tuple(triangle))
    print(len(unique_triangles))


def get_largest_set(nodes):
    unique_sets = set()
    for node in nodes.values():
        name = node.name
        connections = list(node.connections)
        largest_network = get_largest_network(connections, nodes)
        largest_network.append(name)
        largest_network.sort()
        unique_sets.add(tuple(largest_network))

    unique_sets = list(unique_sets)
    unique_sets.sort(key=lambda x: (len(x), x), reverse=True)
    print(",".join(unique_sets[0]))


def get_largest_network(connections, nodes):
    for network_length in range(len(connections), 1, -1):
        for combination in itertools.combinations(connections, network_length):
            combination = list(combination)
            if is_valid_network(combination, nodes):
                return combination


def is_valid_network(combination, nodes):
    for i in range(0, len(combination)):
        node_i = nodes[combination[i]]
        for j in range(i + 1, len(combination)):
            node_j_name = combination[j]
            if node_j_name not in node_i.connections:
                return False
    return True


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = set()

    def add_connection(self, connection):
        self.connections.add(connection)

    def __str__(self):
        return f"{self.name} -> {self.connections}"


def part_two():
    links = read_input()
    nodes = organize_nodes(links)
    get_largest_set(nodes)


def read_input():
    links = []
    with open('input.txt', 'r') as file:
        data = file.read().splitlines()
        for line in data:
            links.append(line.split("-"))

    return links


if __name__ == '__main__':
    part_one()
    part_two()
