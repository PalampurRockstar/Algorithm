from src.main.python.algo.medium.tree.model.node import Node

# https://leetcode.com/problems/cousins-in-binary-tree

import collections


# standared solution
def isCousins(self, root, x, y):
    nodes = collections.defaultdict(list)
    queue = [(root, 0, 0)]
    while queue:
        node, level, parent = queue.pop(0)
        nodes[node.val] = [level, parent]

        if node.left:
            queue.append((node.left, level + 1, node.val))
        if node.right:
            queue.append((node.right, level + 1, node.val))

    if nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]:
        return True

    return False


# my solution
def isCousins(root: Node, x: int, y: int):
    res = False

    def search(node: Node, x: int, y: int):
        if not node: return float("-inf"), float("-inf")
        if node.val == x: return 0, float("-inf")
        if node.val == y: return float("-inf"), 0

        rx, ry = search(node.right, x, y)
        lx, ly = search(node.left, x, y)

        if find_any(rx, ly):return rx + 1, ly + 1
        elif find_any(lx, ry):return lx + 1, ry + 1
        else:return float("-inf"), float("-inf")

    def find_any(x, y):
        nonlocal res
        if x > 0 and y > 0 and x == y:res = True
        elif x > -1 or y > -1:return True
        return False

    search(root, x, y)
    return res


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(15)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

node1 = root.left.right
node2 = root.right.right

if isCousins(root, node1.val, node2.val):
    print("Yes")
else:
    print("No")
