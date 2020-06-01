class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def reverseLinkedList(self):
        current = self.head
        prev = None
        while(current):
            next1 = current.next
            current.next = prev
            prev = current
            current = next1
        self.head = current
    def printLinkedList(self):
        node = self.head
        while(node):
            print node.data
            node = node.next
            
linked = LinkedList()
linked.head = Node(1)
linked.head.next = Node(2)
linked.head.next.next = Node(3)
linked.printLinkedList()
linked.reverseLinkedList()
linked.printLinkedList()
#did not get output        