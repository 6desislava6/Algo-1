class PouringGlass:

    @staticmethod
    def pouring_glass(C1, C2, C3, W1, W2, W3, goal):
        start = (W1, W2, W3)
        if goal in start:
            return True
        if goal > W1 + W2 + W3:
            return False

        explored = set()
        paths = [[start]]

        # Making a tree
        while len(paths) != 0:
            path = paths.pop(0)
            last_node = path[-1]
            next_nodes = PouringGlass.next(C1, C2, C3, last_node[0], last_node[1], last_node[2])
            for (node, action) in next_nodes.items():
                if node not in explored:
                    explored.add(node)
                    path2 = path + [action, node]
                    if goal in node:
                        return path2
                    else:
                        paths.append(path2)
        return False

    @staticmethod
    def next(C1, C2, C3, W1, W2, W3):
        # All possible combinations...
        # There's probably a better way, but naaah
        next_nodes = {}
        if W1 + W2 <= C2:
            next_nodes.update({(0, W1 + W2, W3): '1 -> 2'})
        else:
            next_nodes.update({(W1 - (C2 - W2), C2, W3): '1 -> 2'})

        if W1 + W3 <= C3:
            next_nodes.update({(0, W2, W1+W3): '1 -> 3'})
        else:
            next_nodes.update({(W1 - (C3 - W3), W2, C3): '1 -> 3'})

        if W1 + W2 <= C1:
            next_nodes.update({(W1 + W2, 0, W3): '2 -> 1'})
        else:
            next_nodes.update({(C1, W2 - (C1 - W1), W3): '2 -> 1'})

        if W2 + W3 <= C3:
            next_nodes.update({(W1, 0, W2+W3): '2 -> 3'})
        else:
            next_nodes.update({(W1, W2 - (C3 - W3), C3): '2 -> 3'})

        if W1 + W3 <= C1:
            next_nodes.update({(W1 + W3, W2, 0): '3 -> 1'})
        else:
            next_nodes.update({(C1, W2, W3 - (C1 - W1)): '3 -> 1'})

        if W2 + W3 <= C2:
            next_nodes.update({(W1, W2+W3, 0): '3 -> 2'})
        else:
            next_nodes.update({(W1, C2, W3 - (C2 - W2)): '3 -> 2'})

        return next_nodes


def main():
    capacities = [4, 7, 6]
    water = [2, 5, 4]
    print(PouringGlass.pouring_glass(capacities[0], capacities[1], capacities[2], water[0], water[1], water[2], 1))

if __name__ == '__main__':
    main()


