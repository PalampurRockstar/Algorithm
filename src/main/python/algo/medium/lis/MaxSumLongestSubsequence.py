import sys


def find(arr):
    if len(arr) == 0: return 0
    dp = [0] * len(arr)
    dp[0] = arr[0]
    M = -sys.maxsize
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                M = max(M, dp[j] + arr[i])
        dp[i] = M
    print(dp)
    return dp[-1]


arr = [1, 101, 2, 3, 100, 4, 5]
print(find(arr))
