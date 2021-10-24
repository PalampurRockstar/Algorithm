import sys

#Leet code tested
def findByTabulation(coins, target):
    mat = [[sys.maxsize - 1 if i == 0 and j != 0 else 0 for j in range(target + 1)] for i in range(len(coins) + 1)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i == 0:
                continue
            elif j - coins[i - 1] < 0:
                mat[i][j] = mat[i - 1][j]
            else:
                mat[i][j] = min(mat[i][j - coins[i - 1]] + 1, mat[i - 1][j])
    return mat[len(mat) - 1][len(mat[0]) - 1] if mat[len(mat) - 1][len(mat[0]) - 1] != sys.maxsize - 1 else -1


def findByRecMemorization(coins, index, amount, qb):
    if amount == 0: return 0
    if index > len(coins) - 1 or amount < 0: return sys.maxsize
    key = str(index) + ":" + str(amount)
    if key in qb: return qb[key]

    excluding = findByRecMemorization(coins, index + 1, amount, qb)
    if amount >= coins[index]:
        qb[key] = min(findByRecMemorization(coins, index, amount - coins[index], qb) + 1, excluding)
        return qb[key]
    else:
        qb[key] = excluding
        return qb[key]


def findBySingleArray(coins, amount):
    T = [sys.maxsize if i != 0 else 0 for i in range(amount + 1)]
    for i in coins:
        for j in range(i, len(T)):
            T[j] = min(T[j - i] + 1, T[j])
        print(T)

    return T[amount] if T[amount] != sys.maxsize else -1


def findByRecMemorizationWrap(coins, amount):
    result = findByRecMemorization(coins, 0, amount, dict())
    return result if result != sys.maxsize else -1


target = 15
coins = [3, 4, 6, 7, 9]

# target = 9
# coins = [3, 34, 4, 12, 5, 2]

# target=0
# coins = [2]


# print(findByRecMemorizationWrap(coins, target))
# print(findByTabulation(coins, target))
print(findBySingleArray(coins, target))

