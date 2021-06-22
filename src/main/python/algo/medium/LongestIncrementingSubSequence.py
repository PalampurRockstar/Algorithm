def maxSizeList(a, b):
    if len(a) < len(b):
        return b
    else:
        return a


def findByTabulation(input):
    length = len(input)
    T = [[] for i in input]
    totalMax = 0
    totalMaxList = []
    T[0] = [input[0]]
    for i in range(1, length):
        max = 0
        maxIndex = 0
        for j in range(0, i + 1):
            if input[i] >= input[j]:
                if len(T[j]) > max:
                    max = len(T[j])
                    maxIndex = j

        if max != 0:
            T[i] = T[maxIndex] + [input[i]]
        else:
            T[i] = [input[i]]

        if totalMax < len(T[i]):
            totalMax = len(T[i])
            totalMaxList = T[i]
    return totalMaxList

# brute force
def findByRec(start, end, qb):
    key = ":".join(str(x) for x in start + end)
    if key in qb: return qb[key]
    if len(start) == 0: return findByRec([end[0]], end[1:], qb)

    if len(end) == 1:
        qb[key] = start + [end[0]] if end[0] > start[len(start) - 1] else start
        return qb[key]

    else:
        maxLen = findByRec(start, end[1:], qb)
        if end[0] > start[len(start) - 1]:
            qb[key] = maxSizeList(maxLen, findByRec(start + [end[0]], end[1:], qb))
            return qb[key]
        else:
            qb[key] = maxSizeList(maxLen, findByRec([end[0]], end[1:], qb))
            return qb[key]


import sys


def findByTabulationOptimal(input):
    length = len(input)
    T = [sys.maxsize] * length
    links = [-1] * length

    for i in range(length):
        index = ceilIndex(T, input[i])
        if index != -1:
            if index > 0:
                links[i] = input.index(T[index - 1])
            T[index] = input[i]

    index = links.index(max(links))
    result = []
    while index >= 0:
        result.append(input[index])
        index = links[index]

    return result[::-1]


def ceilIndex(T, n):
    length = len(T)
    lb = 0
    rb = length
    while lb <= rb and lb < length and rb > -1:
        mid = int((lb + rb) / 2)
        if T[mid] == n or lb == rb:
            return mid
        elif T[mid] > n:
            if (mid - 1) > -1 and T[mid - 1] < n:
                return mid
            else:
                rb = mid - 1
        else:
            if (mid + 1) < len(T) and T[mid + 1] > n:
                return mid + 1
            else:
                lb = mid + 1
    if rb < 0:
        return 0
    else:
        return -1

# input = [-1, 3, 4, 5, 2]
# input = [2, 5, 1, 8, 3]
# input = [3, 4, -1, 0, 6, 2, 3]
# input = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
input = [10, 22, 9, 33, 21, 50, 41, 60, 80, 3]

print("Result : " + str(findByRec([], input, dict())))
print("Result : " + str(findByTabulation(input)))
print("Result : " + str(findByTabulationOptimal(input)))
