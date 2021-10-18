from src.main.python.algo.medium.tree.model.node import Node

from collections import defaultdict


def solve(node, map={}):
    ll = []

    def traverse(node, l, r, i=0):
        if not node: return 0
        nonlocal ll
        nonlocal map
        if l and i not in map: map[i] = node.val
        if r and i not in map: map[i] = node.val
        left = traverse(node.left, l, False, i - 1)
        right = traverse(node.right, False, r, i + 1)
        if left == 0 and right == 0: ll.append(node.val)
        return 1

    traverse(node, True, True)
    res1 = sorted(map.items(), key=lambda x: x[0])
    root_part = [k for k, v in res1].index(0)
    val_list = [v for k, v in res1]
    return val_list[root_part:len(val_list) - 1] + ll[::-1] + val_list[1:root_part]


root = Node(1,
            left=Node(2,
                      left=Node(4),
                      right=Node(5)),

            right=Node(3,
                       left=Node(6),
                       right=Node(7))
            )
#           1
#     2          3
# 4       5   6      7
print(solve(root))
