def solve(mat):
    M = 0
    h = len(mat)
    w = len(mat[0])

    def traverse(i, j):

        if -1 < i < h and -1 < j < w and mat[i][j] == 1:
            mat[i][j] = 0
            return traverse(i + 1, j) + \
                   traverse(i, j + 1) + \
                   traverse(i - 1, j) + \
                   traverse(i, j - 1)+1
        else:
            return 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                M = max(M, traverse(i, j))

    return M


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]
print(solve(mat))
