class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

A = Node(24)
B = Node(36)
C = Node(11)
D = Node(10)
E = Node(5)

A.next = B
B.next = C
C.next = D
D.next = E

def count_list(node):
    current = node
    count = 1
    while current.next != None:
        current = current.next
        count += 1
    return count

print(count_list(A))
         