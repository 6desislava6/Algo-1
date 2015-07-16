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


class LowCostFlights:
    max_val = 3000000000000000

    class Vertex:

        def __init__(self, index):
            self.index = index
            self.distance = LowCostFlights.max_val
            self.parent = None

        def __eq__(self, other):
            return self.distance == other.distance

        def __lt__(self, other):
            return self.distance <= other.distance

        def __cmp__(self, other):
            return cmp(self.distance, other.distance)

        def __hash__(self):
            return int(self.index)

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
        self.verteces_queue = PriorityQueue()
        self.verteces = []
        self.connections = connections
        self.distances = [None for i in range(len(table))]
        self.Dijkstra()

    def Dijkstra(self):
        self.initialize_single_source()
        while len(self.verteces_queue.queue) > 0:
            vertex1 = self.verteces_queue.pop()

            self.distances[vertex1.index] = vertex1
            for data in self.connections[vertex1.index]:
                vertex2 = self.verteces[data[0]]
                weight = data[1]

                self.relax(vertex1, vertex2, weight)
            heapq.heapify(self.verteces_queue.queue)

    def relax(self, vertex1, vertex2, weight):
        if vertex2.distance > vertex1.distance + weight:
            vertex2.distance = vertex1.distance + weight
            vertex2.parent = vertex1

    def initialize_single_source(self):
        for i in range(len(self.table)):
            v = LowCostFlights.Vertex(i)
            if i == self.start:
                v.distance = 0
            self.verteces.append(v)
            self.verteces_queue.push(v, v.distance)


def make_connections(table, connections):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] != 0:
                connections[i].append([j, table[i][j]])


def main():
    table = [[0, 9, 0, 3, 2, 0, 0, 0],
             [0, 0, 7, 2, 0, 0, 9, 0],
             [7, 0, 0, 0, 0, 7, 7, 0],
             [0, 2, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 5, 0],
             [0, 3, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 4, 0],
             ]
    connections = [[] for i in range(len(table))]
    make_connections(table, connections)
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
    dijktra = [None for i in range(len(table))]
    for query in queries:
        start = query[0]
        end = query[1]
        if dijktra[start] is not None:
            l = dijktra[start]
            if l.distances[end].distance != LowCostFlights.max_val:
                print(l.distances[end].distance)
            else:
                print('NO WAY')
        else:
            l = LowCostFlights(table, start, connections)
            l.distances
            dijktra[start] = l
            if l.distances[end].distance != LowCostFlights.max_val:
                print(l.distances[end].distance)
            else:
                print('NO WAY')

if __name__ == '__main__':
    main()
