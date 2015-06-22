from QuickSort import QuickSort


class Quadruplets:

        # Returns the number of quadruplets that sum to zero.
        # a - [int]
        # b - [int]
        # c - [int]
        # d - [int]

    @staticmethod
    def binary_search(seq, t):
        min_element = 0
        max_element = len(seq) - 1
        while True:

            if max_element < min_element:
                return None
            m = (min_element + max_element) // 2
            if seq[m] < t:
                min_element = m + 1
            elif seq[m] > t:
                max_element = m - 1
            else:
                return m

    @classmethod
    def zero_quadruplets_count(cls, first_seq, second_seq, third_seq, fourth_seq):
        fourth_seq = QuickSort.quick_sort(fourth_seq)
        quadrupletes = []
        for num1 in first_seq:
            for num2 in second_seq:
                for num3 in third_seq:
                    num4 = -(num1 + num2 + num3)

                    if cls.binary_search(fourth_seq, num4) is not None:
                        quadrupletes.append([num1, num2, num3, num4])

        return len(quadrupletes)


def main():
    first_seq = [5, 3, 4]
    second_seq = [-2, -1, 6]
    third_seq = [-1, -2, 4]
    fourth_seq = [-1, -2, 7]

    print(Quadruplets.zero_quadruplets_count(first_seq, second_seq, third_seq, fourth_seq))

if __name__ == '__main__':
    main()
