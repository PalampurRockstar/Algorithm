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


print(find("babad"))
