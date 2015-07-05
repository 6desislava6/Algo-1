import math


class Median:

    def __init__(self):
        self.minheap = Median.MinHeap()
        self.maxheap = Median.MaxHeap()
        self.median = None

    class MinHeap:

        def __init__(self):
            self.data = []
            self.last = 0

        def get_left_child(self, i, size):
            if 2 * i + 1 >= size:
                return None
            return 2 * i + 1

        def get_right_child(self, i, size):
            if 2 * i + 2 >= size:
                return None
            return 2 * i + 2

        def get_parent(self, i):
            if i == 0:
                return None
            return (i - 1) // 2

        def swap(self, i, j):
            temp = self.data[i]
            self.data[i] = self.data[j]
            self.data[j] = temp

        def bubble_up(self):
            pos = self.last - 1
            while pos > 0 and self.data[self.get_parent(pos)] >= self.data[pos]:
                self.swap(pos, self.get_parent(pos))
                pos = self.get_parent(pos)

        def insert(self, number):
            if len(self.data) == self.last:
                self.data.append(number)
            else:
                self.data[self.last] = number
            self.last += 1
            self.bubble_up()

            return number

        def extract_root(self):
            root = self.data[0]
            self.data[0] = self.data[-1]
            self.data[-1] = None
            self.last -= 1

            self.sink_down(0)
            return root

        def sink_down(self, position):
            right = self.get_right_child(position, self.last)
            left = self.get_left_child(position, self.last)
            if right is None and left is None:
                return
            elif right is None:
                smallest = left
            elif left is None:
                smallest = right
            elif self.data[right] > self.data[left]:
                smallest = left
            else:
                smallest = right

            if self.data[position] >= self.data[smallest]:
                self.swap(position, smallest)
                self.sink_down(smallest)

    class MaxHeap(MinHeap):

        def __init__(self):
            self.data = []
            self.last = 0

        def bubble_up(self):
            pos = self.last - 1
            while pos > 0 and self.data[self.get_parent(pos)] <= self.data[pos]:
                self.swap(pos, self.get_parent(pos))
                pos = self.get_parent(pos)

        def sink_down(self, position):
            right = self.get_right_child(position, self.last)
            left = self.get_left_child(position, self.last)
            if right is None and left is None:
                return
            elif right is None:
                smallest = left
            elif left is None:
                smallest = right
            elif self.data[right] < self.data[left]:
                smallest = left
            else:
                smallest = right

            if self.data[position] < self.data[smallest]:
                self.swap(position, smallest)
                self.sink_down(smallest)

        def insert(self, number):
            if len(self.data) == self.last:
                self.data.append(number)
            else:
                self.data[self.last] = number
            self.last += 1
            self.bubble_up()

            return number

        def extract_root(self):
            root = self.data[0]
            self.data[0] = self.data[-1]
            self.data[-1] = None
            self.last -= 1

            self.sink_down(0)
            return root

    def insert(self, number):
        if self.median is None:
            self.median = self.minheap.insert(number)
            return self.median

        if number >= self.median:

            self.minheap.insert(number)
        else:

            self.maxheap.insert(number)

        if self.minheap.last == self.maxheap.last:
            self.median = self.minheap.data[0]
        elif self.minheap.last + 1 == self.maxheap.last:
            self.median = self.maxheap.data[0]
        elif self.maxheap.last + 1 == self.minheap.last:
            self.median = self.minheap.data[0]
        elif self.minheap.last - self.maxheap.last < -1 or self.minheap.last - self.maxheap.last > 1:
            self.balance()
            self.choose_median()

        return self.median

    def choose_median(self):
        if self.minheap.last == self.maxheap.last:
            self.median = self.minheap.data[0]
        elif self.minheap.last + 1 == self.maxheap.last:
            self.median = self.maxheap.data[0]
        elif self.maxheap.last + 1 == self.minheap.last:
            self.median = self.minheap.data[0]

    def balance(self):
        while math.fabs(self.minheap.last - self.maxheap.last) > 1:
            if self.minheap.last > self.maxheap.last:
                extr = self.minheap.extract_root()
                self.maxheap.insert(extr)
            else:

                extr = self.maxheap.extract_root()
                self.minheap.insert(extr)


def main():
    m = Median()

    nums = [5, 6, 7, 4, 3, 10, 20, 30, 40, 50]
    for num in nums:
        print(m.insert(num))

if __name__ == '__main__':
    main()
