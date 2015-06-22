class PhoneBook:

    # Find the names of people based on their phone numbers.
    # phone_book - [(String, int)]
    # numbers - [int]

    # Making TRIE https://en.wikipedia.org/?title=Trie

    class Node:

        def __init__(self, value, name):
            # Value is a substring of the phone number
            self.name = name
            self.value = value
            # 10 digits
            self.children_nodes = [None for i in range(10)]
            self.isTerminal = False

        def get_value(self):
            return self.value

        def add_node(self, node):
            self.children_nodes[int(node.value[0])] = node

        def get_node(self, value):
            return self.children_nodes[int(value)]

        def __repr__(self):
            return self.name + ' ' + self.value

    @staticmethod
    def insert_node(phone_number, root, name):
        phone_number = str(phone_number)
        current_node = root
        for index in range(len(phone_number)):
            num = phone_number[index]
            result_node = current_node.get_node(num)

            if result_node is None:
                new_node = PhoneBook.Node(phone_number[index:], name)
                if index == len(phone_number) - 1:
                    new_node.isTerminal = True

                current_node.add_node(new_node)
                current_node = new_node
            else:
                current_node = result_node
        return root

    @staticmethod
    def find_node(phone_number, root):

        index = 1
        phone_number = str(phone_number)
        current_node = root.get_node(phone_number[index - 1])
        while current_node is not None and index < len(phone_number):
            current_node = current_node.get_node(phone_number[index])
            index += 1

        if current_node is not None:
            return current_node
        return False

    @staticmethod
    def lookup_names(phone_book, numbers):

        names = []
        root_node = PhoneBook.Node(None, None)
        for name_num in phone_book:
            PhoneBook.insert_node(
                str(name_num[0]), root_node, str(name_num[1]))

        for num in numbers:
            node = PhoneBook.find_node(num, root_node)
            if node:
                names.append(node.name)
        return names


def main():
    print(PhoneBook.lookup_names(
        [(1, "Stanislav"), (15, "Rado"), (1566, "Rado"), (6, "Ivan"), (8, "Ivan")], [15, 8, 1566]))

if __name__ == '__main__':
    main()
