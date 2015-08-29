class Change:

    def __init__(self, coins_denominations, total_sum):
        self.total_sum = total_sum
        self.coins_denominations = coins_denominations
        self.table_ways = [
            [None for x in range(total_sum + 1)] for y in range(len(self.coins_denominations))]

    def make_combinations(self):
        # Initialize the table!
        for i in range(len(self.coins_denominations)):
            self.table_ways[i][0] = 1

        # making the first row
        for i in range(1, self.total_sum + 1):
            if i % self.coins_denominations[0] == 0:
                self.table_ways[0][i] = 1
            else:
                self.table_ways[0][i] = 0

        for i in range(1, len(self.table_ways)):
            for j in range(1, self.total_sum + 1):
                if j < self.coins_denominations[i]:
                    self.table_ways[i][j] = self.table_ways[i - 1][j]
                else:
                    self.table_ways[i][j] = self.table_ways[
                        i - 1][j] + self.table_ways[i][j - self.coins_denominations[i]]

        return self.table_ways[len(self.coins_denominations) - 1][self.total_sum]


def main():
    coins_denominations = [1, 2, 5, 10, 20, 50, 100]
    total_sum = 25
    ch = Change(coins_denominations, total_sum)
    print(ch.make_combinations())

if __name__ == '__main__':
    main()
