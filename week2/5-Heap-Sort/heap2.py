class HeapSort:

    @classmethod
    def get_left_child(cls, i, size):
        if 2 * i + 1 >= size:
            return None
        return 2 * i + 1

    @classmethod
    def get_right_child(cls, i, size):
        if 2 * i + 2 >= size:
            return None
        return 2 * i + 2

    @staticmethod
    def get_parent(i):
        if i == 0:
            return None
        return (i - 1) // 2

    @staticmethod
    def swap(numbers, i, j):
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp

    @classmethod
    def make_min_heap(cls, numbers, end_index, start):
        index = end_index
        while end_index >= start:
            cls.heapify(numbers, start, end_index)
            index -= 1
        return numbers

    @classmethod
    def heapify(cls, numbers, start, lenght):
        while cls.get_left_child(start, lenght) is not None:
            left_child = cls.get_left_child(start, lenght)
            right_child = cls.get_right_child(start, lenght)
            min_child = None

            if right_child is None or numbers[left_child] < numbers[right_child]:
                min_child = left_child
            else:
                min_child = right_child

            print('{} -> {}'.format(numbers[start], numbers[min_child]))
            cls.swap(numbers, start, min_child)
            start = min_child

    # Sorts a sequence of integers.
    @staticmethod
    def sort(sequence):
        i = len(sequence) // 2
        while i >= 1:
            HeapSort.make_min_heap(sequence, i, 0)
            print(sequence)
            i -= 1


def main():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    HeapSort.make_min_heap(arr, len(arr), 0)
    #HeapSort.sort(arr)
    print(arr)

if __name__ == '__main__':
    main()
