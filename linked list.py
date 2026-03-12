# Linked List sederhana

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# membuat node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# menghubungkan node
node1.next = node2
node2.next = node3

# menampilkan linked list
current = node1
while current:
    print(current.data)
    current = current.next