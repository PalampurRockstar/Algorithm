# https://leetcode.com/problems/remove-nth-node-from-end-of-list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head, k):
    fast = head
    count = 0
    prev = None  # is required
    slow = None  # is required
    while fast:
        count += 1
        if count >= k:
            if slow:
                prev = slow
                slow = slow.next
            else:
                slow = head
        fast = fast.next

    if prev:
        prev.next = slow.next
    else:
        return slow.next
    return head


# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head = ListNode(1, ListNode(2))
head = solve(head, 2)
while head:
    print(head.val)
    head = head.next
