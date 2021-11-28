import math
from collections import defaultdict


def solve(arr):
    ul = max(arr) + 1
    UNION = [-1] * ul

    def find_parent(x):
        while UNION[x] != -1: x = UNION[x]
        return x

    def union(x, y):
        x_p = find_parent(x)
        y_p = find_parent(y)
        if x_p != y_p:
            UNION[x_p] = y_p

    for v in arr:
        for i in range(2, int(math.sqrt(v)) + 1):
            if v % i == 0: union(v, i), union(v, v // i)
    ans = defaultdict(lambda: 0)
    MAX = 0
    for v in arr:
        ans[find_parent(v)] += 1
        MAX = max(MAX, ans[find_parent(v)])
    return MAX


arr = [4, 6, 15, 35]
arr = [20, 50, 9, 63]
arr = [2, 3, 6, 7, 4, 12, 21, 39]

print(solve(arr))
