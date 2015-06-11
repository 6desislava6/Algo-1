class Vector:
    capacity_beginning = 32

    def __init__(self):
        self.capacity = Vector.capacity_beginning
        self.container = [None] * self.capacity
        self.size = 0

    def double_itself_if_neccessary(self):
        if self.size == self.capacity:
            self.capacity *= 2
            # Double its size
            container_new = [None] * self.size
            # Copy itself
            for i in range(self.size):
                container_new[i] = self.container
            self.container = container_new

    def add(self, element):
        self.double_itself_if_neccessary()
        self.size += 1
        self.container[self.size] = element

    def insert(self, element, index):
        self.double_itself_if_neccessary()
        container_new = []

        for i in range(index):
            container_new[i] = self.container[i]

        container_new[index] = element

        for i in range(index, self.size):
            container_new[i+1] = self.container[i]

        self.container = container_new
        self.size += 1

    def get(self, index):
        return self.container[index]

    def remove(self, index):
        container_new = []

        for i in range(index):
            container_new[i] = self.container[i]

        for i in range(index, self.size - 1):
            container_new[i] = self.container[i+1]

        self.container = container_new
        self.size -= 1

    def get_size(self):
        return self.size

    def get_capacity(self):
        self.capacity

    def pop(self):
        popped = self.container[self.size - 1]
        self.container[self.size - 1] = None
        return popped
