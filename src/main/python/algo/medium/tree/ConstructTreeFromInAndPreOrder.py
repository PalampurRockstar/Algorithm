class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(IN, POST):
    if len(IN) == 0 or len(POST) == 0: return None
    pos = IN.index(POST.pop())
    return Node(IN[pos], left=solve(IN[:pos], POST[:pos]), right=solve(IN[pos + 1:], POST[pos:]))


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
res = solve(inorder, postorder)


def traverse(node):
    if node:
        traverse(node.left)
        print(node.val)
        traverse(node.right)


traverse(res)
