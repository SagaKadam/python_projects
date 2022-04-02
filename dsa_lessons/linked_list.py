class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        print(self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        print(node, data)

    def print(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
        

if __name__ == '__main__':
    root = LinkedList()
    root.insert_at_beginning(5)
    root.insert_at_beginning(12)
    # root.print()