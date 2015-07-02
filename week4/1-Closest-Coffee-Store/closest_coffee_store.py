class ClosestCoffeeStore:

    # Finds the closest coffee store to a point.
    # graph - [[bool]]
    # starting_point - int
    # is_coffee_store - [bool]


    @staticmethod
    def closestCoffeeStore(graph, is_coffee_store, starting_point):
        queue_vertexes = [starting_point]
        discovered_vertexes = [starting_point]
        previous = [None for i in range(len(graph))]

        while len(queue_vertexes) != 0:
            vertex = queue_vertexes.pop()
            # vertex_vertex = ClosestCoffeeStore.
            if is_coffee_store[vertex] == 1:
                path = ''
                current = vertex
                while current is not None:
                    path += ' >- ' + str(previous[current])
                    current = previous[current]
                print(path[::-1])
                return vertex

            for neighbour in ClosestCoffeeStore.get_neighbours(graph, vertex):
                if neighbour not in discovered_vertexes:
                    previous[neighbour] = vertex
                    queue_vertexes.append(neighbour)
                    discovered_vertexes.append(neighbour)

        return -1

    @staticmethod
    def get_neighbours(graph, vertex):
        neighbours = []
        for i in range(len(graph[vertex])):
            if graph[vertex][i] == 1:
                neighbours.append(i)
                print(neighbours)
        return neighbours


def main():
    graph = [[0, 1, 0, 1 ,0, 0],
             [1, 0, 1, 0 ,0, 0],
             [0, 1, 0, 0 ,1, 0],
             [1, 0, 0, 0 ,0, 0],
             [0, 0, 1, 0 ,0, 1],
             [0, 0, 0, 0 ,1, 0]]
    is_coffee_store = [0, 0, 1, 0, 0, 1]
    starting_point = 0


    print(ClosestCoffeeStore.closestCoffeeStore(graph, is_coffee_store, starting_point))

if __name__ == '__main__':
    main()
