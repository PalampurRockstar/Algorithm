import collections


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def createNodes(arr):
    map = {}
    prev = None
    for i, v in reversed(list(enumerate(arr))):
        node = Node(v[0], prev)
        map[i] = (v[1], node)
        prev = node
    print()
    for k, v in map.items():
        if v[0] in map:
            v[1].random = map[v[0]][1]
    return prev


def printList(node):
    print("-------")
    while node:
        print(node.val, end="\t:\t")
        print(str(node)[59:], end="\t:\t")
        print(str(node.next)[59:], end="\t:\t")
        print(str(node.random)[59:])
        node = node.next
    print("-------")
