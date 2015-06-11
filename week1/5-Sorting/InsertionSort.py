def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current = numbers[i]
        j = i - 1
        while (j >= 0):
            if (current >= numbers[j]):
                # If it's not smaller -> just change it
                numbers[j + 1] = current
                break
            else:
                # Shift to the right
                numbers[j + 1] = numbers[j]
            j -= 1
    return numbers


def main():
    numbers = [1, 9, 5, 6,  2, 6, 3, 4, 7]
    print(insertion_sort(numbers))

    numbers = [3, 8, 1, 2, 9, 5, 7]
    print(insertion_sort(numbers))


if __name__ == '__main__':
    main()
