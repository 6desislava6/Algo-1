class BuildScript:

    class Node:

        def __init__(self, value):
            self.value = value
            self.neighbours = []
            self.previous = None

        def add_neighbour(self, node):
            self.neighbours.append(node)

        def set_previous(self, node):
            self.previous = node

        def __str__(self):
            return str(self.value)

        def __repr__(self):
            return str(self.value)

    @staticmethod
    def build_script(number_of_projects, projects, wanted_project, dependencies):
        data = BuildScript.make_graph(projects, dependencies, wanted_project)

        if not data:
            return "BUILD ERROR"

        graph = data[0]
        wanted_project_node = data[1]
        return BuildScript.go_down(graph, wanted_project_node)

    @staticmethod
    def go_down(graph, wanted_project_node):
        # TO DO ERROR!
        # Двойни връзки в правенето на графа още?
        starting_point = wanted_project_node
        checked = []
        stack = [starting_point]
        leaves = []
        while len(stack) != 0:
            current_node = stack.pop(0)
            for node in current_node.neighbours:
                if node not in stack:
                    stack.append(node)

            if len(current_node.neighbours) == 0 or BuildScript.check_if_subset(leaves, current_node.neighbours):
                if current_node not in leaves:
                    leaves.append(current_node)
            else:
                stack.append(current_node)

            # if len(stack) >= len(graph):
              #  break
        return leaves

    @staticmethod
    def make_graph(projects, dependencies, wanted_project):
        nodes = []
        for project in projects:
            nodes.append(BuildScript.Node(project))
            if project == wanted_project:
                wanted_project_node = nodes[-1]

        for i in range(len(dependencies)):
            for j in range(1, len(dependencies[i])):
                index_node = projects.index(dependencies[i][j])

                if nodes[i] in nodes[index_node].neighbours or nodes[i].value == nodes[index_node].value:
                    return False
                nodes[i].add_neighbour(nodes[index_node])
                nodes[index_node]

        return [nodes, wanted_project_node]

    @staticmethod
    def check_if_subset(bigset, smallset):
        for el in smallset:
            if el not in bigset:
                return False

        return True


def main():
    number_of_projects = 5
    projects = ['Extensions', 'Interface',
                'Core', 'Common', 'Networking', 'BabaTi']
    wanted_project = 'Interface'
    dependencies = [
        [3, 'Common', 'Core', 'Networking'],
        [5, 'Core', 'Common', 'Extensions', 'Networking', 'BabaTi'],
        [1, 'Networking'],
        [1, 'Core'],
        [2, 'Core', 'Common'],
        [3, 'Common', 'Core', 'Networking']]
    print(BuildScript.build_script(
        number_of_projects, projects, wanted_project, dependencies))

if __name__ == '__main__':
    main()
