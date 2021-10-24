from src.main.python.algo.medium.tree.model.node import Node


def construct(arr, types, S=[], prev=None):
    node = Node(arr[0])
    S.append(node)
    for n, t in zip(arr[1:], types[1:]):
        if t == 'N' and S:
            prev = Node(n)
            S[-1].left = prev
            S.append(prev)
        else:
            if prev == S[-1].left:
                S[-1].right = Node(n)
                prev = S.pop()
            else:
                prev = Node(n)
                S[-1].left = prev
    return node


def pre_order(node):
    if not node: return None
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)


arr = [10, 30, 20, 5, 15]
types = ['N', 'N', 'L', 'L', 'L']

arr = [10, 30, 20, 5, 15]
types = ['N', 'N', 'L', 'L', 'L']
root = construct(arr, types)
pre_order(root)
