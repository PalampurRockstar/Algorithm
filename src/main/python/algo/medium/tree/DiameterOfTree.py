# https://leetcode.com/problems/diameter-of-binary-tree
from src.main.python.algo.medium.tree.model.node import Node


def solve(root):
    def dia(root):
        if root == None: return 0, -1
        ld, lh = dia(root.left)
        rd, rh = dia(root.right)
        return max(max(rd, ld), lh + rh + 2), max(lh, rh) + 1
    return dia(root)[0]


root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)

print(solve(root))
