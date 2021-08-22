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
    r = []
    findPart(arr, dp, 0, [], r)
    return r


def findPart(arr, dp, i, found, result):
    l = len(arr)
    if i >= l: return result.append(found)

    for j in range(i, l):
        if dp[i][j]:
            findPart(arr, dp, j + 1, found + [arr[i:j + 1]], result)
    return


def find(arr, found=[], result=[]):
    l = len(arr)
    if l == 0: return result.append(found)
    for i in range(1, l + 1):
        if arr[0:i] == arr[0:i][::-1]:
            find(arr[i:], found + [arr[0:i]], result)
    return result


def partition(arr, found=[], result=[]):
    l = len(arr)
    if l == 0: return result.append(found)
    for i in range(1, l + 1):
        if arr[0:i] == arr[0:i][::-1]:
            find(arr[i:], found + [arr[0:i]], result)
    return result


arr = 'abccbc'
arr = 'aab'
print(findWrap(arr))
print(partition(arr))
