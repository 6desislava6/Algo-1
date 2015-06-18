class BirthdayRanges:

    def _sort_ranges(ranges):
        pass

    @staticmethod
    def _swap(ranges, i, j):
        temp = ranges[i]
        ranges[i] = ranges[j]
        ranges[j] = temp
# returns the position of the pivot

    @classmethod
    def _make_partition(cls, ranges, begining, end):
        pivot = ranges[begining][0]
        firstly_opened = begining + 1
        lastly_closed = begining

        for i in range(begining + 1, end):

            # Open an element
            if ranges[i][0] < pivot:
                cls._swap(ranges, i, firstly_opened)
                lastly_closed = firstly_opened
                firstly_opened += 1
            else:
                continue
        cls._swap(ranges, begining, lastly_closed)

        # returns position of the pivot
        return lastly_closed

    @classmethod
    def quick_sort(cls, ranges, begining, end):
        # End of the recursion
        if end - begining <= 1:
            return
        pivot_index = cls._make_partition(ranges, begining, end)
        cls.quick_sort(ranges, begining, pivot_index)
        cls.quick_sort(ranges, pivot_index + 1, end)
        return ranges
    # Returns a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]

    @classmethod
    def birthdays_count(cls, birthdays, ranges):
        results = [0 for ran in ranges]
        # Sort ranges first - quick sort
        ranges = cls.quick_sort(ranges, 0, len(ranges))
        print(ranges)
        # N birthdays,  binary search ln(n) -> nln(n)
        for bday in birthdays:

            low = 0
            high = len(ranges) - 1
            mid = (low + high) // 2

            while low <= high and ranges[low][0] <= bday and ranges[high][1] >= bday:
                mid = (low + high) // 2
                if ranges[mid][0] > bday:
                    high = mid
                elif ranges[mid][0] < bday:
                    low = mid + 1
                    if ranges[mid][1] >= bday:
                        results[mid] += 1

                else:
                    # If they are equal, start going through the equal elements

                    current_index = mid
                    # Upper side
                    # * * * * *  ->
                    # * * * * *  X * * * * *
                    while ranges[current_index][0] == bday:
                        if ranges[current_index][1] >= bday:
                            results[current_index] += 1
                        current_index += 1

                    # Down side
                    # * * * * *  ->
                    # * * * * *  X * * * * *
                    current_index = mid - 1
                    while ranges[current_index][0] == bday:
                        if ranges[current_index][1] >= bday:
                            results[current_index] += 1
                        current_index -= 1

                    high = current_index

        return results


def main():

    ranges = [[3, 4], [5, 6], [1, 2], [1, 2],
              [1, 2], [1, 2], [100, 101], [60, 63]]

    birthdays = [1, 6, 6, 1, 3, 6, 6, 6, 63, 6, 7, 10, 1, 1]

    print(BirthdayRanges.birthdays_count(birthdays, ranges))

if __name__ == '__main__':
    main()
