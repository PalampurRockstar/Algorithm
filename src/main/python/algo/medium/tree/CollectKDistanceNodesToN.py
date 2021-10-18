from src.main.python.algo.medium.tree.model.node import Node


def solve(node, toFind, k_distance):
    res = []

    def search(node):
        if not node: return float('-inf')
        if toFind == node.val:
            collect(node, k_distance, True, True)
            return k_distance - 1
        else:
            l = search(node.left)
            r = search(node.right)
            if r > -1:
                collect(node, r, True, False)
                return r - 1 if r - 1 >= 0 else float('-inf')
            if l > -1:
                collect(node, l, False, True)
                return l - 1 if l - 1 >= 0 else float('-inf')

    def collect(node, k, right, left):
        if not node: return None
        if k == 0: return res.append(node.val)
        if right: collect(node.left, k - 1, True, True)
        if left: collect(node.right, k - 1, True, True)

    search(node)
    return res


root = Node(3,
            Node(5,
                 Node(6),
                 Node(2,
                      Node(7),
                      Node(4))),
            Node(1,
                 Node(0),
                 Node(8)))
# print(solve(root, 5, 2))
root = Node(0,
            Node(1,
                 Node(3),
                 Node(2)))
print(solve(root, 2, 1))
