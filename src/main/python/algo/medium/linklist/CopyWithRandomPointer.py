from src.main.python.algo.medium.linklist.model import Node, createNodes, printList


# https://leetcode.com/problems/copy-list-with-random-pointer/

def copy(head):
    current = head
    while current:
        newNode = Node(current.val, current.next)
        current.next = newNode
        current = newNode.next
    current = head
    printList(head)

    while current and current.next:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    realCurrent = head
    printList(head)
    newHead = Node(0)
    newCurrent = newHead

    while realCurrent and realCurrent.next:
        newCurrent.next, realCurrent.next = realCurrent.next, realCurrent.next.next
        newCurrent = newCurrent.next
        realCurrent = realCurrent.next
    return newHead.next


node_array = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# node_array = [[3, None], [3, 0], [3, None]]
head = createNodes(node_array)
printList(head)

head = copy(head)
printList(head)
