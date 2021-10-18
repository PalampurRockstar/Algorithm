import sys

def findByRecIndexedWrap(input, target):
    resultList = []
    findByRecIndexed(input, 0, target, [], resultList)
    return resultList


def findByRec(input, target):
    if target == 0:return 1
    if len(input) == 0 or target < 0:return -sys.maxsize

    excluding = findByRec(input[1:], target)
    if target >= input[0]:
        including = findByRec(input[1:], target - input[0])
        return max(including + excluding, max(including, excluding))

    return excluding


def findByRecIndexed(input, index, target, found, resultList):
    if target == 0: return resultList.append(found)

    if target < 0 or index >= len(input): return
    findByRecIndexed(input, index + 1, target, found, resultList)
    if target >= input[index]:
        findByRecIndexed(input, index + 1, target - input[index], found + input[index:index + 1], resultList)


def findByTabulation(coins, target):
    mat = [[0 if j == 0 else -1 for j in range(target + 1)] for i in range(len(coins) + 1)]

    for i in range(len(mat)):
        for j in range(0, len(mat[0])):
            if i == 0 or j == 0:
                continue
            else:
                rstAmt = j - coins[i - 1]
                if rstAmt == 0:
                    mat[i][j] = 1
                if rstAmt != j and rstAmt > -1 and mat[i - 1][rstAmt] != -1:
                    if mat[i - 1][j] != -1:
                        mat[i][j] = mat[i - 1][j] + max(mat[i - 1][rstAmt], mat[i][j])
                    else:
                        mat[i][j] = max(mat[i - 1][rstAmt], mat[i][j])
                elif mat[i - 1][j] != -1:
                    mat[i][j] = mat[i - 1][j]
    return mat[len(mat) - 1][len(mat[0]) - 1]


target = 10
input = [1, 2, 3, 4, 5]
target = 10
input = [2, 3, 5, 6, 8, 10]
# target = 5
# input = [1, 2, 3, 4, 0]
# target = 7
# input = [2, 5, 6, 7]
#
# target = 3
# input = [2]
#
# target = 0
# input = [1]

#Not tested with leet code test cases.
print(findByRec(input, target))
print(findByRecIndexedWrap(input, target))
print(findByTabulation(input, target))
