class Roots:
    # How many digits we want
    ROUND = 5

    # Finds the square root of a number using binary search.
    # number - int
    @staticmethod
    def square_root(number):
        low = 0
        high = number

        while(low < high):
            mid = low + (high - low)/2
            squared = mid * mid

            if number - squared < 0.00001 and number - squared > 0:
                return round(mid, Roots.ROUND)
            elif squared > number:
                high = mid
            else:
                low = mid


def main():

    print(Roots.square_root(37))

if __name__ == '__main__':
    main()
