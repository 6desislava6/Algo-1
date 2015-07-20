import random


class RandSet:

    def __init__(self):
        self.limit = 16
        self.data = [[False, 0, None] for i in range(self.limit)]
        self.size = 0
        self.added = set()

    def _double_itself(self):
        self.limit = self.limit * 2
        old_data = self.data
        self.data = [[False, 0, None] for i in range(self.limit)]
        self.size = 0

        for elements in old_data:
            if elements[0]:
                for index in range(2, elements[1] + 2):
                    self.insert(elements[index])

    def hash_element(self, x):
        x = ((x >> 16) ^ x) * 0x45d9f3b
        x = ((x >> 16) ^ x) * 0x45d9f3b
        x = ((x >> 16) ^ x)
        return x % self.limit

    def insert(self, x):
        hashed = self.hash_element(x)

        # Collision
        if self.data[hashed][0]:
            print('Collision')
            for index in range(self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    print('element already there')
                    return
            print('inserting element ' + str(x))
            self.data[hashed].append(x)
            self.data[hashed][1] += 1
        # No collision
        else:
            print('inserting element ' + str(x))
            self.data[hashed] = [True, 1, x]
        # Changing size

        self.added.add(hashed)
        self.size += 1
        if self.size == self.limit:
            self._double_itself()

    def remove(self, x):
        hashed = self.hash_element(x)
        if not self.data[hashed][0]:
            print('Element not in the set')
            return
        else:
            for index in range(2, 2 + self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    self.data[hashed][index] = None

                    self.data[hashed][1] -= 1
                    if self.data[hashed][1] == 0:
                        self.data[hashed][0] = False

                    self.size -= 1
                    print('Removed element')
                    self.added.remove(hashed)

                    return
            print('Nothing removed, something went wrong')
            return

    def contains(self, x):
        hashed = self.hash_element(x)
        if not self.data[hashed][0]:
            print('Element not found')
            return False
        else:
            for index in range(2, 2 + self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    print('Element found')
                    return True
            print('Element not found')
            return False

    def get_rand_integer(self):
        num = random.sample(self.added, 1)[0]
        random_index = random.randint(0, self.data[num][1])
        return  self.data[num][random_index + 1]


def main():
    r = RandSet()
    for i in range(100):
        r.insert(i)

    for i in range(100):
        r.contains(i)

    print(r.contains(10000))

    r.remove(1)
    r.contains(6)
    r.contains(1)
    print(r.get_rand_integer())
    print(r.get_rand_integer())
    print(r.get_rand_integer())
    print(r.get_rand_integer())
    print(r.get_rand_integer())
    print(r.get_rand_integer())


if __name__ == '__main__':
    main()

