import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    # insert priority to -priority can change to max priority queue
    def push(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def pop(self):
        return heapq.heappop(self.queue)[1]

    def __str__(self):
        return str(self._queue)


class Navigation:
    max_val = 3000000000000000

    class Vertex:

        def __init__(self, index):
            self.index = index
            self.distance = Navigation.max_val
            self.parent = None

        def __eq__(self, other):
            return self.distance == other.distance

        def __lt__(self, other):
            return self.distance <= other.distance

        def __repr__(self):
            if self.parent is not None:
                return '|Vertex {}, distance = {}, parent = {}|'.format(self.index, self.distance, self.parent.index)
            else:
                return '|Vertex {}, distance = {}, parent = NULL|'.format(self.index, self.distance)

    def __init__(self, table, start, connections):
        self.start = start
        self.table = table
        # self.connections[6] are the edges connected to the 6th vertex
        # self.connections[6][0] - connected vertex
        # self.connections[6][1] - weight of the edge
        self.verteces_queue = queue.PriorityQueue()
        self.verteces = []
        self.connections = connections
        self.distances = [None for i in range(len(table))]
        self.Dijkstra()

    def Dijkstra(self):
        self.initialize_single_source()
        while self.verteces_queue.qsize() > 0:
            vertex1 = self.verteces_queue.get_nowait()
            print('chosen')
            print(vertex1)
            self.distances[vertex1.index] = vertex1
            for data in self.connections[vertex1.index]:
                vertex2 = self.verteces[data[0]]
                weight = data[1]

                self.relax(vertex1, vertex2, weight)
                print(vertex2)

    def relax(self, vertex1, vertex2, weight):
        if vertex2.distance > vertex1.distance + weight:


            vertex2.distance = vertex1.distance + weight
            vertex2.parent = vertex1

    def initialize_single_source(self):
        for i in range(len(self.table)):
            v = Navigation.Vertex(i)
            if i == self.start:
                v.distance = 0
            self.verteces.append(v)
            self.verteces_queue.put(v)


def make_connections(table, connections):
    for i in range(len(table)):
        first = table[i][0]
        second = table[i][1]
        weight = table[i][2]
        print('{} {} {}'.format(first, second, weight))
        connections[first].append([second, weight])
        connections[second].append([first, weight])


def main():
    table = [
        [1, 2, 6],
        [1, 3, 2],
        [1, 4, 10],
        [2, 3, 3],
        [2, 4, 3],
        [2, 7, 8],
        [4, 6, 1],
        [6, 7, 2],
        [7, 5, 3],
        [7, 8, 12],
        [8, 5, 6]
    ]
    connections = [[] for i in range(len(table))]
    make_connections(table, connections)
    print(connections[4])
    queries = [
        [0, 5],
        [3, 6],
        [6, 4],
        [3, 2],
        [5, 4],
        [5, 3],
        [7, 6],
        [4, 5],
        [2, 6]]
    start = 1
    l = Navigation(table, start, connections)
    print(l.distances)

if __name__ == '__main__':
    main()
