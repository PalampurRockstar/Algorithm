from src.main.python.algo.medium.tree.model.node import Node

from collections import defaultdict


def solve(node, map=defaultdict(lambda: []), res=[]):
    def traverse(node, i=0):
        if not node: return None
        nonlocal map
        map[i].append(node.val)
        traverse(node.left, i - 1)
        traverse(node.right, i + 1)

    traverse(node)
    for k, v in sorted(map.items(), key=lambda x: x[0]):
        res.append(v)
    return res


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
