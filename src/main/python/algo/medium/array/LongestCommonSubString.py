def solve(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for j in range(l2)] for i in range(l1)]
    M = float('-inf')
    for i in range(l1):
        for j in range(l2):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif s1[i] == s2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                M = max(M, dp[i][j])
    return M


s1 = "abcde"
s2 = "ace"

print(solve(s1, s2))
