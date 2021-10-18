from src.main.python.algo.medium.tree.model.node import Node


def solve(node, S=[], prev=None):
    if not node: return None
    S.append(node)
    while S:
        if S[-1].right == prev:
            prev = S.pop()
            print(prev.val)
        elif S[-1].left == prev:
            if S[-1].right:
                prev = S[-1].right
                S.append(S[-1].right)
        elif S[-1].left:
            prev = S[-1].left
            S.append(S[-1].left)
        else:
            prev = S.pop()
            print(prev.val)


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
solve(root)
