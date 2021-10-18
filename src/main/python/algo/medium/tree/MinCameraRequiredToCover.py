from src.main.python.algo.medium.tree.model.node import Node
#https://leetcode.com/problems/binary-tree-cameras/

def solve(node):
    res = 0

    def state(node):
        nonlocal res
        if not node: return 1
        r = state(node.right)
        l = state(node.left)
        if l == -1 or r == -1:
            res += 1
            return 0
        elif l == 0 or r == 0:
            return 1
        else:
            return -1

    s = state(node)
    return res if s != -1 else res + 1


root = Node(1,Node(4,Node(3),Node(5)))

print(solve(root))
