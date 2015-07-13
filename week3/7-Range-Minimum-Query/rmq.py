import math


class RMQ:

    # sets the value at index

    def __init__(self, array):
        self.array = array
        self.data_smallest = []
        self.make_data_smallest()

        # Segment tree!

    def make_data_smallest(self):
        # Determing how long the last level must be
        last_level_size = math.log(len(self.array), 2)
        if last_level_size != int(last_level_size):
            last_level_size = math.ceil(last_level_size)

        last_level_size = int(math.pow(2, last_level_size))
        size = 2 * last_level_size - 1
        self.data_smallest = [0 for n in range(size)]
        index = len(self.data_smallest) - last_level_size
        i = 0

        # Making the first level
        while i < len(self.array):
            self.data_smallest[index + i] = self.array[i]
            i += 1

        # Making all levels
        start = len(self.data_smallest) - last_level_size
        end = size - 1
        while start > 0:
            self.build_level2(start, end)
            end = start - 1
            start //= 2

    def build_level2(self, start, end):
        index = start
        while index <= end:
            parent = self.get_parent(index)
            if self.data_smallest[index] < self.data_smallest[index + 1]:
                self.data_smallest[parent] = self.data_smallest[index]
            else:
                self.data_smallest[parent] = self.data_smallest[index + 1]
            index += 2

    @classmethod
    def get_left_child(i, size):
        if 2 * i + 1 >= size:
            return None
        return 2 * i + 1

    @classmethod
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

    def set(self, index, value):
        pass

    # returns the minimum value in a range
    def min(self, startIndex, endIndex):
        pass


def main():
    r = RMQ([19, 11, 15, 4, 7 ,13, 11, 2])
    print(r.data_smallest)


if __name__ == '__main__':
    main()
