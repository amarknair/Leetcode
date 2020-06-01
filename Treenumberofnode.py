class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def nodeNumber(node):
    if node is None:
        return 0
    else:
        return 1 + nodeNumber(node.left) + nodeNumber(node.right)
def count_nodes(node):
    if node:
        print node.data
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)   

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print nodeNumber(root)