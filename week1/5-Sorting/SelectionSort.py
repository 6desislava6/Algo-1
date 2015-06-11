def selection_sort(numbers):
    min_num = numbers[0]
    for i in range(len(numbers) - 1):
        min_num = numbers[i]
        for j in range(i, len(numbers)):
            if min_num > numbers[j]:
                temp = min_num
                min_num = numbers[j]
                numbers[j] = temp
        if numbers[i] > min_num:
            temp = numbers[i]
            numbers[i] = min_num
            min_num = temp
    return numbers


def main():
    numbers = [1, 2, 3, 4]
    print(selection_sort(numbers))
    numbers = [1, 9, 5, 6,  2, 6, 3, 4, 7]
    numbers = [3, 8, 1, 2, 9, 5, 7]

    print(selection_sort(numbers))

if __name__ == '__main__':
    main()
