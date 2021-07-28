import sys


def findByRec(input, target):
    if len(input) == 0 or target == 0: return 0
    excluding = findByRec(input[1:], target)
    if target >= input[0][0]:
        including = findByRec(input[1:], target - input[0][0]) + input[0][1]
        return max(including, excluding)
    else:
        return excluding


def findByRec2(input, target):
    if target == 0: return 0
    if len(input) == 0 or target < 0: return -sys.maxsize
    return max(findByRec2(input[1:], target),findByRec2(input[1:], target - input[0][0]) + input[0][1])


def findByTabulation(input, target):
    length = len(input)
    mat = [[0 for j in range(target + 1)] for i in range(length + 1)]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0 or j == 0:
                continue
            elif j - input[i - 1][0] < 0:
                mat[i][j] = mat[i - 1][j]
            else:
                including = j - input[i - 1][0]
                mat[i][j] = max(mat[i - 1][j], mat[i - 1][including] + input[i - 1][1])

    return mat[len(mat) - 1][len(mat[0]) - 1]


def printMat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end="\t")
        print()


input = [
    [2, 15],
    [5, 14],
    [1, 10],
    [3, 45],
    [4, 30]
]
print(findByRec(input, 7))
print(findByRec2(input, 7))
print(findByTabulation(input, 7))
