# Write a Python program to create a singly linked list, append some items and iterate through the list.

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self):
        node = Node()
        self.head = node


if __name__ == '__main__':
    pass