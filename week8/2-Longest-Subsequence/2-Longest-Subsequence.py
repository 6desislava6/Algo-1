class LongestSubsequence:

    def __init__(self, count, numbers):
        self.count = count
        self.numbers = numbers

    def find_longest_subseq(self):
        resulting = [1 for x in range(self.count)]
        previous = [x for x in range(self.count)]
        i = 1
        j = 0

        for i in range(1, self.count):
            for j in range(i):
                if self.numbers[i] > self.numbers[j] and resulting[i] < resulting[j] + 1:
                    resulting[i] = resulting[j] + 1
                    previous[i] = j

        max_num = -9999999999999
        max_num_index = 0

        for i in range(self.count):
            if max_num < resulting[i]:
                max_num = resulting[i]
                max_num_index = i

        print(max_num)
        sequence = []
        for i in range(max_num):
            num = self.numbers[max_num_index]
            max_num_index = previous[max_num_index]
            sequence.append(num)
        print(sequence)


def main():
    l = LongestSubsequence(10, [6, 1, 5, 3, 7, 1, 2, 5, 7, 4])
    l.find_longest_subseq()


if __name__ == '__main__':
    main()
