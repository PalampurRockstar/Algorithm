from src.main.python.algo.medium.tree.model.node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def in_order(root):
    S = [root]
    while S[-1].left: S.append(S[-1].left)
    while S:
        current = S.pop()
        print(current.val)
        if current.right:
            S.append(current.right)
            while S[-1].left: S.append(current.left)


in_order(root)
