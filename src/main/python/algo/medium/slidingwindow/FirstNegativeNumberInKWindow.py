# https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/


import collections


def find(arr, k):
    DQ = collections.deque()
    res = []
    for i, v in enumerate(arr):
        if v < 0: DQ.append(v)
        if i + 1 >= k:
            res.append(DQ[0] if DQ else 0)
            if DQ and DQ[0] == arr[i - k + 1]: DQ.popleft()
    return res


arr = [-8, 2, 3, -6, 10]
k = 2
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

print(find(arr, k))
