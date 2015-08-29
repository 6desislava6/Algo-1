class LCS:

    def __init__(self, input1, input2):
        self.find_lcs(input1, input2)

    def print_table(self, rows, cols, table):
        for i in range(rows):
            x = ''
            for j in range(cols):
                x += ' {}'.format(table[i][j])
            print(x)

    def find_lcs(self, input1, input2):
        rows = len(input2) + 1
        cols = len(input1) + 1
        table = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(1,  len(input2) + 1):
            for j in range(1, len(input1) + 1):
                if input1[j - 1] == input2[i - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = 0

        # self.print_table(rows, cols, table)
        data = self.find_biggest_element(rows, cols, table)
        self.find_substring(table, data[0], data[1], data[2], input1)

    def find_biggest_element(self, rows, cols, table):
        max_x = 0
        max_y = 0
        max_num = -999999999999
        for i in range(rows):
            for j in range(cols):
                if table[i][j] > max_num:
                    max_x = i
                    max_y = j
                    max_num = table[i][j]

        return [max_x, max_y, max_num]

    def find_substring(self, table, max_x, max_y, max_num, input1):
        num = max_num
        sentence = input1[max_y - 1]
        while num > 0:
            sentence += input1[max_y - 1]
            max_x -= 1
            max_y -= 1
            num = table[max_x][max_y]

        print(sentence[::-1])

def main():
    l = LCS('The quick brown fox jumps over the lazy dog', 'A fox which is quick and brown jumps over the dog which is lazy')

if __name__ == '__main__':
    main()
