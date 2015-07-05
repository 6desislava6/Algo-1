import math

class Median:

    def __init__(self):
        self.maxheap = Median.MaxHeap()
        self.minheap = Median.MinHeap()
        self.median = None

    class Node:

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.parent = None

        def add_left(self, left):
            self.left = left

        def add_right(self, right):
            self.right = right

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_value(self):
            return self.value

        def __repr__(self):
            return 'node with value {}'.format(self.value)

        @staticmethod
        def swap_nodes(node1, node2):
            temp_node = node1
            node1.value = node2.value
            node2.value = temp_node.value

    class MinHeap:

        def __init__(self):
            self.root = None
            self.lastly_inserted = self.root
            self.count = 0

        def bubble_up(self, node):
            parent_node = node.parent
            while parent_node is not None:
                if parent_node.value > node.value:
                    Median.Node.swap_nodes(parent_node, node)
                parent_node = parent_node.parent

        def insert_node(self, value):
            if self.root is None:
                self.root = Median.Node(value)
                self.count = 1
                new_node = self.root
                self.median = self.root
                self.lastly_inserted = new_node
                return new_node

            new_node = Median.Node(value)
            if math.log(self.count, 2) - int(math.log(self.count, 2)) < 0.01:
                # making a new level
                # finding the leftmost element
                mostleft = self.root
                while mostleft.left is not None:
                    mostleft = mostleft.left
                mostleft.left = new_node
                new_node.parent = mostleft
            elif self.count % 2 == 0:
                self.lastly_inserted.parent.left = new_node
                new_node.parent = self.lastly_inserted.parent
            else:
                if self.count == 1:
                    self.lastly_inserted.left = new_node
                    new_node.parent = self.lastly_inserted
                else:
                    self.lastly_inserted.parent.right = new_node
                    new_node.parent = self.lastly_inserted.parent
            self.count += 1
            self.lastly_inserted = new_node

            self.bubble_up(new_node)
            print('new_node')
            print(new_node)
            return new_node

        def extract_root(self):
            root = self.root
            Median.Node.swap_nodes(self.root, self.lastly_inserted)
            # Многото нещо с ln и тн
            # TO DO
            self.bubble_down(root)
            if math.log(self.count, 2) - int(math.log(self.count, 2)) + 1 < 0.01:
                # making a new level
                # finding the leftmost element
                mostright = self.root
                while mostright.right is not None:
                    mostright = mostright.right
                self.lastly_inserted = mostright

            elif self.count % 2 == 0:
                self.lastly_inserted.parent.left = new_node
                new_node.parent = self.lastly_inserted.parent
            else:
                if self.count == 1:
                    self.lastly_inserted.left = new_node
                    new_node.parent = self.lastly_inserted
                else:
                    self.lastly_inserted.parent.right = new_node
                    new_node.parent = self.lastly_inserted.parent
            self.count += 1
            self.lastly_inserted = new_node

        def bubble_down(self, node):
            if node.right is None and node.left is not None:
                smallest = node.left
            if node.left is None:
                return

            if node.left.value > node.right.value:
                smallest = node.right
            else:
                smallest = node.right

            if node.value > smallest.value:
                Median.Node.swap_nodes(node, smallest)
                self.bubble_down(smallest)
            else:
                return

    class MaxHeap(MinHeap):

        def __init__(self):
            self.root = None
            self.lastly_inserted = self.root
            self.count = 0

        def bubble_up(self, node):
            parent_node = node.parent
            while parent_node is not None:
                if parent_node.value < node.value:
                    Median.Node.swap_nodes(parent_node, node)
                parent_node = node.parent

        def bubble_down(self, node):
            if node.right is None and node.left is not None:
                smallest = node.left
            if node.left is None:
                return

            if node.left.value > node.right.value:
                smallest = node.right
            else:
                smallest = node.right

            if node.value <= smallest.value:
                Median.Node.swap_nodes(node, smallest)
                self.bubble_down(smallest)
            else:
                return

# inserts the number and returns the median
    def insert(self, number):
        if self.median is None:
            self.median = self.minheap.insert_node(number)
            return self.median.value

        if number >= self.median.value:
            print('min heap')
            self.minheap.insert_node(number)
        else:
            print('max heap')

            self.maxheap.insert_node(number)

        if self.minheap.count == self.maxheap.count or self.minheap.count - self.maxheap.count == -1 or self.minheap.count - self.maxheap.count == 1:
            return self.minheap.root
        elif self.minheap.count + 1 == self.maxheap.count:
            return self.maxheap.root
        elif self.maxheap.count + 1 == self.minheap.count:
            return self.minheap.root
        elif self.minheap.count - self.maxheap.count < -1 or self.minheap.count - self.maxheap.count > 1:
            print('razlika')
            print(self.minheap.count - self.maxheap.count)
            self.balance()

    def balance(self):
        print('HOPE NOT')


def main():
    m = Median()
    while True:
        n = input()
        print(m.insert(int(n)))

if __name__ == '__main__':
    main()
