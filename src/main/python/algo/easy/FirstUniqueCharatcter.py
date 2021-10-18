# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import defaultdict
import collections


def solve(arr, visited=defaultdict(lambda: 0), DQ=collections.deque([])):
    for i, c in enumerate(arr):
        visited[c] += 1
        DQ.append([i, c])
        while DQ and visited[DQ[0][1]] > 1: DQ.popleft()
    return DQ[0][0] if DQ else -1


def solve(arr, visited=defaultdict(lambda: 0)):
    for c in arr:visited[c] += 1
    for i, c in enumerate(arr):
        if visited[c] == 1: return i
    return -1


# arr = "leetcode"
# print(solve(arr))

arr = "loveleetcode"
print(solve(arr))
