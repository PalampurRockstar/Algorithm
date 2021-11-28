# https://leetcode.com/problems/delete-node-in-a-bst/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node):
    if node:
        print_tree(node.left)
        print(node.val, end="\t")
        print_tree(node.right)


def delete(node, k):
    if node:
        if node.val == k:
            print(node.val)
            if node.left and node.right:
                current = node.right
                while current.left:
                    current = current.left
                delete(node, current.val)
                node.val = current.val
                return node
            elif node.left:
                return node.left
            else:
                return node.right
        elif node.val > k:
            node.left = delete(node.left, k)
        else:
            node.right = delete(node.right, k)
    return node


# root = TreeNode(5, left=TreeNode(3, TreeNode(2), TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
# root = delete(root, 3)
# root = delete(root, 5)
root = TreeNode(50, left=TreeNode(30, right=TreeNode(40)), right=TreeNode(70, left=TreeNode(60), right=TreeNode(80)))
root = delete(root, 50)
print_tree(root)
