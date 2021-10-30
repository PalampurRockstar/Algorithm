# https://leetcode.com/problems/rotting-oranges

import collections


def solve(mat):
    n, m = len(mat), len(mat[0])
    Q = collections.deque([])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1: cnt += 1
            if mat[i][j] == 2: Q.append((i, j))
    res = 0
    while Q:
        for _ in range(len(Q)):
            i, j = Q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and mat[x][y] == 1:
                    mat[x][y] = 2
                    cnt -= 1
                    Q.append((x, y))
        res += 1
    return max(0, res - 1) if cnt == 0 else -1


mat = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
mat = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(solve(mat))
