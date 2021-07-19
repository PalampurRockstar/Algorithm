import sys


# leet code tested
def find(input, k):
    length = len(input)
    if length < 2: return 0
    dp = [[0 for _ in range(length)] for _ in range(k + 1)]
    for i in range(k + 1):
        maxOld = -sys.maxsize
        for j in range(length):
            if i == 0 or j == 0: continue
            maxOld = max(maxOld, dp[i - 1][j - 1] - input[j - 1])
            dp[i][j] = max(input[j] + maxOld, dp[i][j - 1])

    return dp[k][length - 1]

# result=6
k = 3
input = [9, 6, 7, 6, 3, 8]

# result=6
# k = 2
# input = []


print(find(input, k))
