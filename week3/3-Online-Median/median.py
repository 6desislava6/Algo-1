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
                    Node.swap_nodes(parent_node, node)
                parent_node = node.parent

        def insert_node(self, value):
            if self.root is None:
                self.root = Median.Node(value)
                self.count = 1
                self.lastly_inserted = new_node
                return

            new_node = Median.Node(value)
            if math.log(self.count, 2) - int(math.log(self.count, 2)) < 0.01:
                # making a new level
                # finding the leftmost element
                mostleft = self.root
                while mostleft.left is not None:
                    mostleft = mostleft.left
                mostleft.left = new_node
            elif self.count % 2 == 0:
                self.lastly_inserted.parent.left = new_node
            else:
                self.lastly_inserted.parent.right = new_node
            self.count += 1
            self.lastly_inserted = new_node

            self.bubble_up(new_node)
            return new_node

        def extract_root(self):
            root = self.root
            Node.swap_nodes(self.root, self.lastly_inserted)
            # Многото нещо с ln и тн
            # TO DO
            self.bubble_down(root)

        def bubble_down(self, node):
            if node.right is None and node.left is not None:
                smallest = left
            if node.left is None:
                return

            if node.left.value > node.right.value:
                smallest = right
            else:
                smallest = right

            if node.value > smallest.value:
                Node.swap_nodes(node, smallest)
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
                    Node.swap_nodes(parent_node, node)
                parent_node = node.parent



#inserts the number and returns the median
    def insert(self, number):
        if self.median is None:
            self.median = self.minheap.insert_node(number)
            return self.median.value
        if number >= self.median.value:
            self.minheap.insert_node(number)
        else:
            self.maxheap.insert_node(number)

        if self.minheap.count == self.maxheap.count:
            return self.minheap.top

    def balance(self):
        if self.minheap.count + 1 < self.maxheap.count:



