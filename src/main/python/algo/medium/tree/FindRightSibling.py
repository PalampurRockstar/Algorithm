class Node:
    def __init__(self, item, parent):
        self.data = item
        self.left = self.right = None
        self.parent = parent


def findRightSibling(node, level):
    if not node or not node.parent: return None
    while node.parent.right == node or (not node.parent.right and node.parent.left == node):
        if not node.parent: return None
        node = node.parent
        level -= 1
    node = node.parent.right
    while level < 0:
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            break
        level += 1

    if level == 0:
        return node
    return findRightSibling(node, level)
def findRightSibling(node, level):
    if (node == None or node.parent == None):
        return None

        # GET Parent pointer whose right child is not
    # a parent or itself of this node. There might
    # be case when parent has no right child, but,
    # current node is left child of the parent
    # (second condition is for that).
    while (node.parent.right == node or
           (node.parent.right == None and
            node.parent.left == node)):
        if (node.parent == None):
            return None

        node = node.parent
        level -= 1

    # Move to the required child, where
    # right sibling can be present
    node = node.parent.right

    # find right sibling in the given subtree
    # (from current node), when level will be 0
    while (level < 0):

        # Iterate through subtree
        if (node.left != None):
            node = node.left
        elif (node.right != None):
            node = node.right
        else:

            # if no child are there, we cannot
            # have right sibling in this path
            break

        level += 1

    if (level == 0):
        return node

        # This is the case when we reach 9 node
    # in the tree, where we need to again
    # recursively find the right sibling
    return findRightSibling(node, level)

# def solve(node):
#     if not node or not node.parent: return None
#     l = 0
#
#     # go up
#
#     node_is_right = node.parent.right == node
#
#     while node and node.parent:
#         if node_is_right
#         l -= 1
#         node = node.parent


root = Node(1, None)
root.left = Node(2, root)
root.right = Node(3, root)
root.left.left = Node(4, root.left)
root.left.right = Node(6, root.left)
root.left.left.left = Node(7, root.left.left)
root.left.left.left.left = Node(10, root.left.left.left)
root.left.right.right = Node(9, root.left.right)
root.right.right = Node(5, root.right)
root.right.right.right = Node(8, root.right.right)
root.right.right.right = Node(10, root.right.right.right)
root.right.right.right.right = Node(12, root.right.right.right)

# passing 10
res = findRightSibling(root.left.left.left.left, 0)
if (res == None):
    print("No right sibling")
else:
    print(res.data)
