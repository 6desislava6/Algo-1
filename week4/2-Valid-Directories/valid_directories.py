class ValidDirectories:

    @staticmethod
    def isValid(graph):
        all_vertexes = [i for i in range(len(graph))]
        # Visited at all
        visited = []

        while len(all_vertexes) != 0:
            queue_vertexes = []
            # Currently discovered
            discovered_vertexes = []
            starting = all_vertexes.pop()

            queue_vertexes.append(starting)
            discovered_vertexes.append(starting)
            not_reached_visited = True

            while len(queue_vertexes) != 0 and not_reached_visited:
                vertex = queue_vertexes.pop()

                for neighbour in ValidDirectories.get_subdirectories(graph, vertex):
                    if neighbour not in discovered_vertexes:
                        queue_vertexes.append(neighbour)
                        discovered_vertexes.append(neighbour)
                        all_vertexes.remove(neighbour)
                    else:
                        return False

                    if neighbour in visited:
                        not_reached_visited = False
                    visited.append(neighbour)
        return True

    @staticmethod
    def get_subdirectories(graph, vertex):
        subdirectories = []
        for i in range(len(graph[vertex])):
            if graph[vertex][i] == 1:
                subdirectories.append(i)
                print(subdirectories)
        return subdirectories


def main():
    graph = [[0, 1, 0, 1, 0, 2],
         [0, 0, 2, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 2, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

    print(ValidDirectories.isValid(graph))

if __name__ == '__main__':
    main()
