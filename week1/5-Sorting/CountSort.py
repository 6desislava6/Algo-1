def max_num(array):
    max_num = array[0]
    for i in range(len(array)):
        if array[i] > max_num:
            max_num = array[i]
    return max_num


def counting_sort(array, maxval):
    sorted_array = []
    possible_values_count = maxval + 1
    values_counter = [0] * possible_values_count

    # Making keys
    for num in array:
        values_counter[num] += 1

    for a in range(possible_values_count):
        for c in range(values_counter[a]):
            sorted_array.append(a)

    return sorted_array


def counting_sort_no_maxVal(array):
    max_value = max_num(array)
    return counting_sort(array, max_value)


def main():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(counting_sort_no_maxVal(numbers))

if __name__ == '__main__':
    main()
