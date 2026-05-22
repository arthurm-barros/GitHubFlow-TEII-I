# Problema 01: crie uma lista encadeada

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node1.next = node2
node2.next = node3

linked_list = LinkedList(node1)