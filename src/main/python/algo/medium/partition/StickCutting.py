import sys


def findByEachCut(price):
    l = len(price)
    mp = [0] * (l + 1)  # optimal price/max price on this location

    for i in range(1, l + 1):
        mp[i] = price[i - 1]
        for j in range(1, i):
            mp[i] = max(mp[i], price[j - 1] + mp[i - j])
    return mp[l]


def findByOptimalLeftRight(price):
    l = len(price)
    mp = [0] * (l + 1)  # optimal price/max price on this location
    # original price vs max(j)+max(i-j) vs max(j+1)+max(i-j+1)
    for i in range(1, l + 1):
        mp[i] = price[i - 1]  # original price
        for j in range(1, int(i / 2)):
            mp[i] = max(mp[i], mp[j] + mp[i - j])  # left mp[j] and mp[i - j] right
    return mp[l]


def findByIncludeExcludeWrap(arr):
    l = len(arr)
    qb = [[None for _ in range(l + 1)] for _ in range(l)]
    result = findByIncludeExclude(arr, 0, l, qb)
    return result if result != -sys.maxsize else 0


def findByIncludeExclude(arr, index, target, qb):
    if target == 0: return 0
    if index >= len(arr): return -sys.maxsize
    cl = index + 1  # current length
    if qb[index][target]: return qb[index][target]
    qb[index][target] = findByIncludeExclude(arr, index + 1, target, qb)
    if cl <= target:
        qb[index][target] = max(qb[index][target], findByIncludeExclude(arr, index, target - cl, qb) + arr[cl - 1])
    return qb[index][target]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print(findByEachCut(arr))
print(findByOptimalLeftRight(arr))
print(findByIncludeExcludeWrap(arr))
