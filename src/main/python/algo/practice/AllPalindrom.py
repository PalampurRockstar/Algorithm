def find(arr):
    l = len(arr)
    dp = [[False for j in range(l)] for i in range(l)]
    res = []
    for g in range(l):
        for j in range(g, l):
            i = j - g
            if g == 0:
                dp[i][j] = True
            elif g == 1:
                dp[i][j] = True if arr[i] == arr[j] else False
            else:
                dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else False
            if dp[i][j]:
                res.append(arr[i:j + 1])
    return res


def find(arr, found=[], index=0, qb=dict(), result=[]):
    l = len(arr)
    if index == l: return result.append(found)
    if index in qb: return qb[index]
    for i in range(index, l):
        if arr[index:i + 1] == arr[index:i + 1][::-1]:
            find(arr, found + [arr[index:i + 1]], i + 1, qb, result)
    qb[index] = result
    return result


print(find(arr='abccbc'))
