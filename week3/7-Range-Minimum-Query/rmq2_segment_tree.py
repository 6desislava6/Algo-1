import math


class RMQ:

    # sets the value at index
    # A node at index y is parent of a node at index x,
    # iff y can be obtained by removing last set bit from binary
    # representation of x.
    max_num = 10000000000000000000000

    def __init__(self, array):
        self.array = array
        self.size = self.determine_size()

        self.tree = [RMQ.max_num for i in range(self.size)]
        self.make_tree(0, len(self.array) - 1, 0)

    def determine_size(self):
        last_level_size = math.log(len(self.array), 2)
        if last_level_size != int(last_level_size):
            last_level_size = math.ceil(last_level_size)

        last_level_size = int(math.pow(2, last_level_size))
        return 2 * last_level_size - 1

    def make_tree(self, low, high, pos):
        if low == high:
            self.tree[pos] = self.array[low]
            return
        mid = (low + high) // 2
        left = self.get_left_child(pos, self.size)
        right = self.get_right_child(pos, self.size)

        self.make_tree(mid + 1, high, right)
        self.make_tree(low, mid, left)

        if left is not None and right is None:
            self.tree[pos] = self.tree[left]
        if right is not None and left is None:
            self.tree[pos] = self.tree[right]
        if right is not None and left is not None:
            self.tree[pos] = min(
                self.tree[left], self.tree[right])

    # qlow and qhigh are the wanted range
    def range_min_query(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:
            # total overlap
            return self.tree[pos]
        if qlow > high or qhigh < low:
            # no overlap
            return RMQ.max_num
        # partial overlap
        mid = (low + high) // 2
        left = self.get_left_child(pos, self.size)
        right = self.get_right_child(pos, self.size)

        return min(self.range_min_query(qlow, qhigh, low, mid, left), self.range_min_query(qlow, qhigh, mid + 1, high, right))

    def rmq(self, qlow, qhigh):
        return self.range_min_query(qlow, qhigh, 0, len(self.array) - 1, 0)

    def updateValueUtil(self, pos, low, high, i, new_val):
        if i < low or i > high:
            return

        if low == high:
            self.tree[pos] = new_val
            return

        left = self.get_left_child(pos, self.size)
        right = self.get_right_child(pos, self.size)

        if left is not None and right is not None:
            mid = (low + high) // 2
            if i <= mid:
                self.updateValueUtil(left, low, mid, i, new_val)
            else:
                self.updateValueUtil(right, mid + 1, high, i, new_val)

            self.tree[pos] = min(self.tree[left], self.tree[right])

    def update(self, i, new_val):
        self.updateValueUtil(0, 0, len(self.array) - 1, i, new_val)
        self.array[i] = new_val

    @staticmethod
    def get_left_child(i, size):
        if 2 * i + 1 >= size:
            return None
        return 2 * i + 1

    @staticmethod
    def get_right_child(i, size):
        if 2 * i + 2 >= size:
            return None
        return 2 * i + 2

    @staticmethod
    def get_parent(i):
        if i == 0:
            return None
        return (i - 1) // 2

    def swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp


def main():
    r = RMQ([-1, 3, 4, 0, 2, 1, 7])
    print(r.tree)
    print(r.rmq(2, 3))

    r.update(0, 6)
    print(r.tree)

    r.update(2, 6)
    print(r.tree)

    r.update(1, 6)
    print(r.tree)
    r.update(3, 6)
    print(r.tree)
    r.update(4, 6)
    print(r.tree)
    r.update(5, 6)
    print(r.tree)
    r.update(6, 6)
    print(r.tree)

    print(r.array)
    print(r.tree)

    r1 = RMQ(r.array)
    print(r1.tree)


if __name__ == '__main__':
    main()
