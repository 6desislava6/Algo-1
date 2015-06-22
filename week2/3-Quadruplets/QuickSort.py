# Demo explaining
# http://me.dt.in.th/page/Quicksort/


class QuickSort:

    @staticmethod
    def swap(numbers, i, j):
        temp = numbers[i]
        numbers[i] = numbers[j]
        numbers[j] = temp

# returns the position of the pivot
    @classmethod
    def make_partition(cls, numbers, begining, end):
        pivot = numbers[begining]
        firstly_opened = begining + 1
        lastly_closed = begining

        for i in range(begining + 1, end):

            # Open an element
            if numbers[i] < pivot:
                cls.swap(numbers, i, firstly_opened)
                lastly_closed = firstly_opened
                firstly_opened += 1
            else:
                continue
        cls.swap(numbers, begining, lastly_closed)

        # returns position of the pivot
        return lastly_closed

    # Sorts a list.
    @classmethod
    def sorts_list(cls, numbers, begining, end):
        # End of the recursion
        if end - begining <= 1:
            return
        pivot_index = cls.make_partition(numbers, begining, end)
        cls.sorts_list(numbers, begining, pivot_index)
        cls.sorts_list(numbers, pivot_index + 1, end)
        return numbers

    # Returns a new, sorted list.
    @classmethod
    def quick_sort(cls, numbers):
        # making copy of the array/list in order to work with it
        new_numbers = list(numbers)
        return cls.sorts_list(new_numbers, 0, len(new_numbers))
