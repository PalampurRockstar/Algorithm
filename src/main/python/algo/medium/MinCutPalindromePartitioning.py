import sys


def findWrap(arr):
    l = len(arr)
    dp = [[False for _ in range(l)] for _ in range(l)]
    for g in range(l):
        for j in range(g, l):
            i = j - g
            if g == 0:
                dp[i][j] = True
            elif g == 1:
                dp[i][j] = 1 if arr[i] == arr[j] else False
            else:
                dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else False
    r = findMinPart(arr, dp, 0)
    return r - 1 if r != sys.maxsize else 0


def findMinPart(arr, dp, i):
    if i >= len(arr): return 0
    m = sys.maxsize
    for j in range(i, len(arr)):
        if dp[i][j]: m = min(m, findMinPart(arr, dp, j + 1) + 1)
    return m


def findByReverseWrap(arr):
    res = findByReverse(arr)
    return res - 1 if res != sys.maxsize else 0


def findByReverse(arr):
    l = len(arr)
    if l == 0: return 0
    m = sys.maxsize
    for i in range(1, l + 1):
        if arr[0:i] == arr[0:i][::-1]:
            m = min(m, findByReverse(arr[i:]) + 1)
    return m


arr = 'abccbc'
print(findWrap(arr))
print(findByReverseWrap(arr))
