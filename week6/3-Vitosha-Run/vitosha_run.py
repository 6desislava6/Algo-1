import heapq
import math


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


class VitoshaRun:
    max_val = 100000000000000000000000000000

    class Vertex:

        def __init__(self, index_x, index_y, altitude):
            self.index_x = index_x
            self.index_y = index_y
            self.altitude = altitude
            self.time = VitoshaRun.max_val
            self.parent = None

        def __eq__(self, other):
            return self.index_x == other.index_x and self.index_y == other.index_y

        def __lt__(self, other):
            return self.time <= other.time

        def __cmp__(self, other):
            return cmp(self.time, other.time)

        def __hash__(self):
            return int(self.index_x)

        def __repr__(self):
            if self.parent is not None:
                return '|Vertex {} {}, altitude = {}, parent = {} {} time = {} |'.format(self.index_x, self.index_y, self.altitude, self.parent.index_x,self.parent.index_y, self.time)
            else:
                return '|Vertex {} {}, altitude = {}, parent = NULL time = {}|'.format(self.index_x, self.index_y, self.altitude, self.time)

    def __init__(self, table, start_x, start_y, end_x, end_y, size):
        self.size = size

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

        self.table = table

        self.verteces_queue = PriorityQueue()
        self.visited = []

        self.verteces = [
            [None for i in range(self.size)] for j in range(self.size)]
        self.distances = [None for i in range(len(table))]

        self.print_path(self.Dijkstra())

    def print_path(self, end):
        print('PATH')
        print(end)
        last = end.parent

        while(last):
            print(last)
            last = last.parent

    def Dijkstra(self):
        # self.initialize_single_source()
        start = VitoshaRun.Vertex(
            self.start_x, self.start_y, self.table[self.start_x][self.start_y])
        start.time = 0
        self.verteces[self.start_x][self.start_y] = start

        self.verteces_queue.push(start, start.time)
        while len(self.verteces_queue.queue) > 0:
            vertex1 = self.verteces_queue.pop()
            self.visited.append(vertex1)
            if vertex1.index_x == self.end_x and vertex1.index_y == self.end_y:
                return vertex1
            neighbours = self.make_vertices(vertex1.index_x, vertex1.index_y)
            for vertex2 in neighbours:
                self.relax(vertex1, vertex2)
            heapq.heapify(self.verteces_queue.queue)

    def relax(self, vertex1, vertex2):
        if (vertex2.altitude - vertex1.altitude) > 0:
            weight = (vertex2.altitude - vertex1.altitude) + 1
        else:
            weight = -(vertex2.altitude - vertex1.altitude) + 1

        if vertex2.time > vertex1.time + weight:
            vertex2.time = vertex1.time + weight
            vertex2.parent = vertex1

    def make_vertices(self, index_x, index_y):
        neighbours = []
        coordinates = [
            (0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
        for coords in coordinates:
            new_coords = [index_x + coords[0], index_y + coords[1]]
            if new_coords[0] >= self.size or new_coords[0] < 0:
                continue
            elif new_coords[1] >= self.size or new_coords[1] < 0:
                continue
            else:
                if self.verteces[new_coords[0]][new_coords[1]] is None:
                    self.verteces[new_coords[0]][new_coords[1]] = VitoshaRun.Vertex(
                        new_coords[0], new_coords[1], self.table[new_coords[0]][new_coords[1]])

                if self.verteces[new_coords[0]][new_coords[1]] not in self.visited:
                    self.verteces_queue.push(self.verteces[new_coords[0]][
                                             new_coords[1]], self.verteces[new_coords[0]][new_coords[1]].time)
                    neighbours.append(
                        self.verteces[new_coords[0]][new_coords[1]])
        return neighbours


def main():
    table = [[5, 3, 1, 4, 6, 7],
             [8, 1, 5, 6, 3, 1],
             [9, 8, 5, 1, 5, 2],
             [0, 9, 1, 3, 5, 8],
             [5, 2, 5, 7, 1, 7],
             [9, 8, 1, 4, 3, 9]]
    v = VitoshaRun(table, 0, 0, 5, 5, 6)


if __name__ == '__main__':
    main()
