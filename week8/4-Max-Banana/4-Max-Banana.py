def max_banana(table):

    max_up = len(table)
    max_left = len(table[0])
    values = [[-1 for i in range(max_left)] for j in range(max_up)]
    max_count = table[max_up - 1][0] + recurse(values, [0, 0], table, 0, 0)
    print(max_count)


def recurse(values, position, table, up, left):
    # up - колко пъти нагоре
    # left - колко пъти наляво се е предвижил
    x = position[0]
    y = position[1]

    if x > len(table) or y >= len(table[0]):
        return 0

    if values[up][left] != -1:
        return values[up][left]

    go_up = go_left = 0

    if len(table) - (x + 1) - 1 >= 0:
        go_up = recurse(
            values, [x + 1, y], table, up + 1, left) + table[len(table) - (x + 1) - 1][y]

    if y + 1 < len(table[0]):
        go_left = recurse(
            values, [x, y + 1], table, up, left + 1) + table[len(table) - x - 1][y + 1]

    values[up][left] = max(go_up, go_left)
    return values[up][left]


def main():
        table = [[9, 3, 4, 1, 5],
                 [1, 7, 1, 9, 1],
                 [4, 2, 1, 3, 4],
                 [2, 1, 2, 2, 1],
                 [1, 3, 2, 1, 7]]
        max_banana(table)


if __name__ == '__main__':
    main()
