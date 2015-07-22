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
        x = ((x >> 16) ^ x)
        return x % self.limit

    def insert(self, x):
        hashed = self.hash_element(x)

        # Collision
        if self.data[hashed][0]:
            for index in range(self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    return
            self.data[hashed].append(x)
            self.data[hashed][1] += 1
        # No collision
        else:
            self.data[hashed] = [True, 1, x]
        # Changing size

        self.added.add(hashed)
        self.size += 1
        if self.size == self.limit:
            self._double_itself()

    def remove(self, x):
        hashed = self.hash_element(x)
        if not self.data[hashed][0]:
            return
        else:
            for index in range(2, 2 + self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    self.data[hashed][index] = None

                    self.data[hashed][1] -= 1
                    if self.data[hashed][1] == 0:
                        self.data[hashed][0] = False

                    self.size -= 1
                    self.added.remove(hashed)

                    return
            return

    def contains(self, x):
        hashed = self.hash_element(x)
        if not self.data[hashed][0]:
            return False
        else:
            for index in range(2, 2 + self.data[hashed][1]):
                if self.data[hashed][index] == x:
                    return True
            return False


def main():
    list1 = [2, 666666, 5, 10, 3, 1, 2222222222222222234444444444444444444444444402345]
    list2 = [7, 13, 3, 9, 2, 55, 47, 666666,10, 2222222222222222234444444444444444444444444402345]
    list3 = [666666,42, 2, 3, 2222222222222222234444444444444444444444444402345, 2222222222222222234444444444444444444444444402341]

    r1 = RandSet()
    r2 = RandSet()
    r3 = RandSet()

    for el in list1:
        r1.insert(el)
    for el in list2:
        r2.insert(el)
    for el in list3:
        r3.insert(el)

    #print(r1.data)
    #print(r2.data)
    #print(r3.data)

    for index in range(len(r1.data)):
        for index_inside in range(r1.data[index][1]):
            if r1.data[index][index_inside + 2] in r2.data[index][2:] and r1.data[index][index_inside + 2] in r2.data[index][2:] and r1.data[index][index_inside + 2] is not None:
                print(r1.data[index][2 + index_inside])

if __name__ == '__main__':
    main()
