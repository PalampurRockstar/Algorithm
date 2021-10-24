from src.main.python.algo.medium.tree.model.node import Node


def solve(node):
    if not node: return 0
    r = solve(node.right)
    l = solve(node.left)
    node.val, res = r + l, node.val
    return res + node.val


def traverse(node):
    if not node: return None
    traverse(node.left)
    print(node.val, end="\t")
    traverse(node.right)


root = Node(10)
root.left = Node(-2)
root.right = Node(6)
root.left.left = Node(8)
root.left.right = Node(-4)
root.right.left = Node(7)
root.right.right = Node(5)

solve(root)
traverse(root)
