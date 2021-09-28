# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/

import collections
import sys


def find(arr, k, DQ=collections.deque(), MIN=sys.maxsize, acc=[]):
    if len(arr) == 0: return 0
    acc = [arr[0]]
    for v in arr[1:]: acc.append(acc[-1] + v)
    for f, v in enumerate(acc):
        while DQ and acc[DQ[-1]] >= v: DQ.pop()
        while DQ and v - acc[DQ[0]] >= k: MIN = min(MIN, (DQ[-1] - DQ.popleft()) + 1)
        DQ.append(f)
    return MIN


arr = [2, 3, 1, 1, -1, 3, 4]
k = 7
print(find(arr, k))
