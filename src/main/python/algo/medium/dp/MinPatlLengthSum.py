# https://leetcode.com/problems/minimum-path-sum/

def solve(mat):
    h = len(mat)
    w = len(mat)
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                mat[i][j] += mat[i][j - 1]
            elif j == 0:
                mat[i][j] += mat[i - 1][j]
            else:
                mat[i][j] += min(mat[i - 1][j], mat[i][j - 1])
    return mat[h - 1][w - 1]


mat = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(solve(mat))
