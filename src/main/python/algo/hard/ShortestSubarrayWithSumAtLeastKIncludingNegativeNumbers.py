import collections
import sys


def find(arr, k):
    length = len(arr)
    if length == 0: return 0
    acc = [0]
    for v in arr:
        acc.append(acc[-1] + v)
    Q = collections.deque([])
    res = sys.maxsize
    for i, v in enumerate(acc):
        while Q and v - acc[Q[0]] >= k: res = min(res, i - Q.popleft())
        while Q and acc[Q[-1]] >= v: Q.pop()
        Q.append(i)
    return res


k = 3
arr = [2, -1, 2, 1]

k = 7
arr = [2, 3, 1, 1, -1, 3, 4]

print(find(arr, k))
