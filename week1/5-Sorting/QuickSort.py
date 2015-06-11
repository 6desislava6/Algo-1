# Demo explaining
# http://me.dt.in.th/page/Quicksort/


def swap(numbers, i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp


# returns the position of the pivot
def make_partition(numbers, begining, end):
    pivot = numbers[begining]
    firstly_opened = begining + 1
    lastly_closed = begining

    for i in range(begining + 1, end):

        # Open an element
        if numbers[i] < pivot:
            swap(numbers, i, firstly_opened)
            lastly_closed = firstly_opened
            firstly_opened += 1
        else:
            continue
    swap(numbers, begining, lastly_closed)

    # returns position of the pivot
    return lastly_closed


# Sorts a list.
def sorts_list(numbers, begining, end):
    # End of the recursion
    if end - begining <= 1:
        return
    pivot_index = make_partition(numbers, begining, end)
    sorts_list(numbers, begining, pivot_index)
    sorts_list(numbers, pivot_index + 1, end)
    return numbers


# Returns a new, sorted list.
def quick_sort(numbers):
    # making copy of the array/list in order to work with it
    new_numbers = list(numbers)
    return sorts_list(new_numbers, 0, len(new_numbers))


def main():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(quick_sort(numbers))
    print(numbers)


if __name__ == '__main__':
    main()
