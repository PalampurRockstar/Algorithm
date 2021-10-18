from src.main.python.algo.medium.tree.model.node import Node


def solve(node, S=[]):
    if not node: return None
    S.append(node)
    while S:
        current = S.pop()
        print(current.val)
        if current.left: S.append(current.left)
        if current.right: S.append(current.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
solve(root)
