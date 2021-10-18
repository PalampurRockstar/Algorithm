from src.main.python.algo.medium.tree.model.node import Node


def solve(node, k):
    res = 0

    def count(node):
        nonlocal res
        if not node: return 0
        l = count(node.left)
        r = count(node.right)
        if l + node.val + r == k: res += 1
        return l + node.val + r
    count(node)
    return res


root = Node(5)
root.left = Node(-10)
root.right = Node(3)
root.left.left = Node(9)
root.left.right = Node(8)
root.right.left = Node(-4)
root.right.right = Node(7)

x = 7
ptr = root

print(solve(root, x))
