def findByRecMemorization(input, indexes, qb):
    left, right = indexes
    key = str(left) + ":" + str(right)
    if key in qb: return qb[key]
    if right < 0 or left > len(input) - 1 or left > right:
        qb[key] = []
        return qb[key]
    if (right - left + 1) == 0 or (right - left + 1) == 1:
        qb[key] = [input[left:right + 1]]
        return qb[key]
    if input[left] == input[right]:
        qb[key] = [input[left]] + findByRecMemorization(input, (left + 1, right - 1), qb) + [input[left]]
        return qb[key]
    else:
        leftList = findByRecMemorization(input, (left, right - 1), qb) + ['_']
        rightList = ['_'] + findByRecMemorization(input, (left + 1, right), qb)
        qb[key] = leftList if len(leftList) > len(rightList) else rightList
        return qb[key]


def findByRec(input):
    length = len(input)
    if length == 0 or length == 1: return [input]
    if input[0] == input[length - 1]:
        return [input[0]] + findByRec(input[1:length - 1]) + [input[0]]
    else:
        leftList = findByRec(input[:length - 1]) + ['_']
        rightList = ['_'] + findByRec(input[1:])
        return leftList if len(leftList) > len(rightList) else rightList


def findByTabulation(input):
    length = len(input)
    mat = [[0 for j in range(length)] for i in range(length)]
    for i in range(length):
        for j in range(length - i):
            k = j + i
            if i == 0:
                mat[j][k] = 1
            elif i == 1:
                if input[j] == input[k]:
                    mat[j][k] = 2
                else:
                    mat[j][k] = 1
            else:
                if input[j] == input[k]:
                    mat[j][k] = mat[j + 1][k - 1] + 2
                else:
                    mat[j][k] = max(mat[j][k - 1], mat[j + 1][k])
    return length - mat[0][length - 1] if mat[0][length - 1] != 0 else -1


def printMat(mat):
    print()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end="\t")
        print()


input = "aabaaba"

print(findByRecMemorization(input, (0, len(input) - 1), dict()).count("_"))
print(findByTabulation(input))
print(findByRec(input).count('_'))
