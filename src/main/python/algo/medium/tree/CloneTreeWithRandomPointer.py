from src.main.python.algo.medium.tree.model.node import Node


def clone(node, cloned=None):
    if not node: return None

    if cloned:
        cloned.val = node.val
    else:
        cloned = Node(node.val)
    cloned.random = node.random
    node.random = cloned
    cloned.left = clone(node.left, cloned.left)
    cloned.right = clone(node.right, cloned.right)
    return cloned


def preorder(node):
    if not node: return
    print(str(node.val) + "\t:\t" + str(node)[59:] + "\t:\t" + str(node.random)[59:])
    preorder(node.left)
    preorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.random = root.right.left.random
root.left.left.random = root.right
root.left.right.random = root
root.right.left.random = root.left.left
root.random = root.left

print("Preorder traversal of the original tree:")
preorder(root)

cloned = clone(root)

print("Preorder traversal of the cloned tree:")
preorder(cloned)
