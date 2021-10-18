from src.main.python.algo.medium.tree.model.node import Node


def solve(root):
    M = float("-inf")

    def get_max_gain(node):
        nonlocal M
        if node is None: return 0
        ls = max(get_max_gain(node.left), 0)
        rs = max(get_max_gain(node.right), 0)
        M = max(M, node.val + ls + rs)
        return node.val + max(ls, rs)

    get_max_gain(root)
    return M


# root = Node(1)
# root.right = Node(3)
# root.left = Node(2)
# root.left.right = Node(5)
# root.left.left = Node(4)


# root = Node(1)
# root.right = Node(3)
# root.left = Node(2)

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.right = Node(7)
root.right.left = Node(15)

print(solve(root))
