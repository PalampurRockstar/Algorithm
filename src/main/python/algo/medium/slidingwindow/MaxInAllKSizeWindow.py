# https://leetcode.com/problems/sliding-window-maximum/

import collections


def find(arr, k, ltr=collections.deque(), b=0, res=[]):
    for f, v in enumerate(arr):
        while ltr and ltr[-1] < v: ltr.pop()
        ltr.append(v)
        if f + 1 >= k:
            res.append(ltr[0])
            if arr[b] == ltr[0]: ltr.popleft()
            b += 1
    return res


arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3

arr = [1, 3, -1, -3, 5, 3, 6, 7]
ki = 3
print(find(arr, k))
