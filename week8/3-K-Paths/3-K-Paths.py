class KPath:

    def __init__(self, graph, start, end, length):
        self.graph = graph
        self.start = start
        self.end = end
        self.length = length
        print(self.count_paths(start, end, graph, length))

    def count_paths(self, start, end, graph, length):
        verteces = len(graph)
        # 3D table
        # 1-st dimension is source
        # 2-nd is destination
        # 3-rd is count of edges between source and destination
        table_counts = [[[0 for x in range(length + 1)] for i in range(verteces)] for j in range(verteces)]

        for k in range(length + 1):
            for i in range(verteces):
                for j in range(verteces):
                    table_counts[i][j][k] = 0
                    if k == 0 and i == j:
                        table_counts[i][j][k] = 1
                    if k == 1 and j in graph[i]:
                        table_counts[i][j][k] = 1
                    if k > 1:
                        for a in range(verteces):
                            if a in graph[i]:
                                table_counts[i][j][
                                    k] += table_counts[a][j][k - 1]

        return table_counts[start][end][length]


def main():
    graph = [[1, 2, 3], [3], [3], []]
    k = KPath(graph, 0, 3, 2)

if __name__ == '__main__':
    main()
