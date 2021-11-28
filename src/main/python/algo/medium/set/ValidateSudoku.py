# https://leetcode.com/problems/valid-sudoku

def solve(mat):
    # column
    for i in range(len(mat[0])):
        visited = set()
        for j in range(len(mat)):
            if mat[j][i] == '.': continue
            if mat[j][i] in visited or int(mat[j][i]) < 1 or int(mat[j][i]) > 9:
                return False
            visited.add(mat[j][i])
    # row
    for i in range(len(mat)):
        visited = set()
        for j in range(len(mat[i])):
            if mat[i][j] == '.': continue
            if mat[i][j] in visited or int(mat[i][j]) < 1 or int(mat[i][j]) > 9:
                return False
            visited.add(mat[i][j])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            visited = set()
            for k in range(3):
                for l in range(3):
                    x = i + k
                    y = j + l
                    if mat[x][y] == '.': continue
                    if mat[x][y] in visited or int(mat[x][y]) > 9 or int(mat[x][y]) < 1:
                        return False
                    visited.add(mat[x][y])
    return True


# def isValidSudoku(board):
#     for i in range(9):
#         nums = 0
#         A = set()
#         for j in range(9):
#             if board[i][j].isnumeric():
#                 A.add(board[i][j])
#                 nums += 1
#         if nums != len(A):
#             print("row")
#             return False
#     for i in range(9):
#         nums = 0
#         A = set()
#         for j in range(9):
#             if board[j][i].isnumeric():
#                 A.add(board[j][i])
#                 nums += 1
#         if nums != len(A):
#             print("col")
#             return False
#     for i in range(3):
#         for j in range(3):
#             nums = 0
#             A = set()
#             for k in range(3):
#                 for m in range(3):
#                     if board[3 * i + k][3 * j + m].isnumeric():
#                         A.add(board[3 * i + k][3 * j + m])
#                         nums += 1
#             if nums != len(A):
#                 return False
#     return True


mat = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]
       ]

# mat = [
#     [".", "8", "7", "6", "5", "4", "3", "2", "1"],
#     ["2", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["3", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["4", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["5", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["6", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["8", ".", ".", ".", ".", ".", ".", ".", "."],
#     ["9", ".", ".", ".", ".", ".", ".", ".", "."]
# ]
# mat = [
#     [".", ".", ".", ".", "5", ".", ".", "1", "."],
#     [".", "4", ".", "3", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
#     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
#     [".", ".", "2", ".", "7", ".", ".", ".", "."],
#     [".", "1", "5", ".", ".", ".", ".", ".", "."],
#     [".", ".", ".", ".", ".", "2", ".", ".", "."],
#     [".", "2", ".", "9", ".", ".", ".", ".", "."],
#     [".", ".", "4", ".", ".", ".", ".", ".", "."]
# ]
print(solve(mat))
