class KPath:

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.DFS(start)

    def DFS(self, start):
        stack = [start]
        discovered = []
        levels = [None for x in range(len(self.graph))]
        levels[start] = 0
        while len(stack) > 0:
            v = stack.pop(0)
            level = levels[v]
            print('v', v)
            print('level', level)
            if v not in discovered:
                discovered.append(v)
                print(discovered)
                for next_vertex in self.graph[v]:
                    if next_vertex not in discovered:
                        levels[next_vertex] = level + 1
                    stack.append(next_vertex)
# DAYMN :D

def main():
    graph = [[0, 1], [0, 2], [0, 3], [1, 3], [2, 3]]
    k = KPath(graph, 0, 1)

if __name__ == '__main__':
    main()
