# https://leetcode.com/problems/add-two-numbers/
def solve(node1, node2):
    carry = 0
    node = None
    head = None
    rss = []
    while node1 or node2:
        sum = str(carry + node1.val + node2.val)
        carry = 0
        if len(sum) > 1:
            carry += int(sum[0])
        rss.append(int(sum[-1]))
        if node:
            node.next = ListNode(int(sum[-1]))
            node = node.next
        else:
            node = ListNode(int(sum[-1]))
            head = node
        node2 = node2.next
        node1 = node1.next
        if node2 or node1:
            if not node2:
                node2 = ListNode(0, None)
            if not node1:
                node1 = ListNode(0, None)
    if carry:
        node.next = ListNode(carry, None)
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


res = solve(ListNode(2, ListNode(4, ListNode(3, None))),
            ListNode(5, ListNode(6, ListNode(4, None))))
while res:
    print(res.val)
    res = res.next
