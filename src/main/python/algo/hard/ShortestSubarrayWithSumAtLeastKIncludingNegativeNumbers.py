#https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
import collections
import sys


def find(arr, K, res=sys.maxsize, Q=collections.deque([]), acc=[0]):
    if len(arr) == 0: return 0
    for v in arr: acc.append(acc[-1] + v)
    for i, v in enumerate(acc):
        while Q and acc[Q[-1]] >= v: Q.pop()
        while Q and v - acc[Q[0]] >= K: res = min(res, (Q[-1] - Q.popleft()) + 1)
        Q.append(i)
    return res if res != sys.maxsize else -1


k = 3
arr = [2, -1, 2, 1]

k = 7
arr = [2, 3, 1, 1, -1, 3, 4]

print(find(arr, k))
