def printAllStairPath(discovered, n):
    if n < 0: return
    if n == 0:
        print(discovered)
    for i in range(1, 4):
        printAllStairPath(discovered + [i], n - i)


def findCountByRec(n, qb):
    if n in qb: return qb[n]
    if n < 0:
        return 0
    if n == 0:
        return 1
    sum = 0
    for i in range(1, 4):
        sum += findCountByRec(n - i, qb)
    qb[n] = sum
    return qb[n]


def findByTabulation(n):
    if n == 0: return 0
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        sum = 0
        for j in range(1, 4):
            index = i - j
            sum += result[index] if index > -1 else 0
        result[i] = sum
    return result[n]


num = 10
printAllStairPath([], num)
print(findCountByRec(num, dict()))
print(findByTabulation(num))
