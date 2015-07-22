class WordDictionary:

    class Node:

        def __init__(self, char):
            # char is a substring of the phone number
            self.char = char
            # 10 digits
            self.children_nodes = [None for i in range(26)]
            self.isTerminal = False

        def get_char(self):
            return self.char

        def add_node(self, node):
            index = ord(node.char[0]) - 97
            self.children_nodes[index] = node

        def get_node(self, char):
            index = ord(char) - 97
            return self.children_nodes[index]

        def __repr__(self):
            return self.char

    def insert_node(self, string):
        current_node = self.root

        for index in range(len(string)):
            char = string[index]
            result_node = current_node.get_node(char)

            if result_node is None:
                new_node = WordDictionary.Node(string[index:])
                if index == len(string) - 1:
                    new_node.isTerminal = True

                current_node.add_node(new_node)
                current_node = new_node
            else:
                current_node = result_node
        return self.root

    def find_node(self, phone_number):
        root = self.root
        index = 1
        phone_number = str(phone_number)
        current_node = root.get_node(phone_number[index - 1])
        while current_node is not None and index < len(phone_number):
            current_node = current_node.get_node(phone_number[index])
            index += 1
            # print(current_node)
        if current_node is not None:
            return True
        return False

    def __init__(self):
        self.root = WordDictionary.Node('')


def main():
    w = WordDictionary()
    w.insert_node('alabala')
    w.insert_node('asdf')
    print(w.find_node('alabala'))
    w.insert_node('aladin')
    print(w.find_node('asdf'))
    print(w.find_node('aladin'))
    w.insert_node('circle')
    print(w.find_node('rectangle'))
    print(w.find_node('square'))




if __name__ == '__main__':
    main()
