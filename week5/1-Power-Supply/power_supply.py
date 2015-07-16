class PowerSupply:

    def __init__(self, data):
        self.vertexes = set()
        self.edges = data
        self.edges.sort(key=lambda x: x[2])
        self.make_vertexes()

    def make_vertexes(self):
        for edge in self.edges:
            self.vertexes.add(edge[0])
            self.vertexes.add(edge[2])

    def remove_paralel_loops(self):
        for
    def Kruskal(self):
        for edge in self.edges:
            pass
def main():
    junction_connections = 12
    data = [[1, 2, 1100],
            [1, 3, 1400],
            [1, 4, 2000],
            [2, 4, 2000],
            [2, 5, 1300],
            [1, 6, 2600],
            [3, 5, 780],
            [5, 4, 1000],
            [3, 4, 900],
            [3, 6, 1300],
            [6, 7, 200],
            [4, 7, 800]]

    p = PowerSupply(data)
    print(p.edges)

if __name__ == '__main__':
    main()
