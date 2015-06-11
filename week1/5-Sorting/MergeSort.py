def merge(first_half, second_half):
    resulting = []
    index_first = 0
    index_second = 0

    # How many elements I added from the first
    added_from_first = 0
    # How many elements I added from the second
    added_from_second = 0

    # Starting sorted merging!
    while len(first_half) - added_from_first > 0 and len(second_half) - added_from_second > 0:
        if first_half[index_first] < second_half[index_second]:
            added_from_first += 1
            resulting.append(first_half[index_first])
            index_first += 1

        else:
            added_from_second += 1
            resulting.append(second_half[index_second])
            index_second += 1

    # Smb has finished
    if len(first_half) - added_from_first > 0:
        for i in range(index_first, len(first_half)):
            resulting.append(first_half[index_first])
            index_first += 1

    else:
        for i in range(index_second, len(second_half)):
            resulting.append(second_half[index_second])
            index_second += 1

    return resulting


def merge_sort(numbers):
    # Bottom of recursion
    if len(numbers) == 1:
        return numbers

    # Else
    middle = len(numbers) // 2

    first_half = numbers[:middle]
    second_half = numbers[middle:]

    # Recursively
    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)

    return merge(sorted_first_half, sorted_second_half)


def main():
    numbers = [1, 9, 5, 6,  2, 6, 3, 4, 7, 1, 9, 5, 6,
               2, 6, 3, 4, 7, 10000, 2342350000, 235363, 764]
    numbers2 = [1, 3, 5]
    numbers1 = [2, 4, 6]
    print(merge(numbers1, numbers2))
    print(merge_sort(numbers))


if __name__ == '__main__':
    main()
