class PhoneNumbers:

    class Node:

        def __init__(self, value):
            self.value = value
            self.neighbours = set()

        def add_neighbour(self, node):
            self.neighbours.add(node)

        def __str__(self):
            return 'node' + str(self.value)

        def __repr__(self):
            return 'node' + str(self.value)

    @staticmethod
    def whom_to_call(number_of_people, phone_numbers, contacts):
        nodes = PhoneNumbers.make_graph(phone_numbers, contacts)
        return PhoneNumbers.DFS(nodes)

    @staticmethod
    def make_graph(numbers, contacts_all):
        nodes = []
        for number in numbers:
            nodes.append(PhoneNumbers.Node(number))

        for i in range(len(contacts_all)):
            for j in range(1, len(contacts_all[i])):
                index_node = numbers.index(contacts_all[i][j])
                nodes[i].add_neighbour(nodes[index_node])

        return nodes

    @staticmethod
    def DFS(graph):
        not_discovered = graph
        discovered_vertexes = []
        components = []
        components_count = 0

        while len(not_discovered) != 0:

            print(not_discovered)
            starting_point = not_discovered.pop()
            currently_discovered = [starting_point]
            stack_vertexes = [starting_point]
            current_component = [starting_point]

            while len(stack_vertexes) != 0:
                vertex = stack_vertexes.pop(0)

                for neighbour in vertex.neighbours:
                    if neighbour not in currently_discovered:
                        stack_vertexes.append(neighbour)
                        currently_discovered.append(neighbour)
                        discovered_vertexes.append(neighbour)
                        not_discovered.remove(neighbour)
                        current_component.append(neighbour)
            components.append(current_component)
            components_count += 1

        print(components)
        return components_count


def main():
    number_of_people = 6
    nodes = [100, 200, 300, 400, 500, 600]
    contacts = [[2, 200, 300],
                [2, 100, 300],
                [2, 100, 200],
                [1, 500],
                [1, 400],
                [0]]
    print(PhoneNumbers.whom_to_call(number_of_people, nodes, contacts))

if __name__ == '__main__':
    main()
