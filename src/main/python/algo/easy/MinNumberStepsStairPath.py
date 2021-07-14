import sys

def findMinCountByRec(n, qb):
    if n < 0: return 0;
    if n == 0: return 1;
    minSteps = sys.maxsize
    if n in qb: return qb[n]
    for i in range(1, 4):
        minSteps = min(findMinCountByRec(n - i, qb), minSteps)
    qb[n] = minSteps + 1
    return qb[n]


def findMinCountByTabulation(n):
    result = [0] * (n + 1)
    result[0] = 1

    for i in range(1, n + 1):
        minSteps = sys.maxsize
        for j in range(1, 4):
            newIndex = i - j
            minSteps = min(result[newIndex] if newIndex > -1 else 0, minSteps)
        result[i] = minSteps + 1
    return result[n]


num = 10
print(findMinCountByRec(num, dict()))
print(findMinCountByTabulation(num))
