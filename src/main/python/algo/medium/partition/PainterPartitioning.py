# https://www.geeksforgeeks.org/painters-partition-problem

def solve_by_tabulation(arr, n, k):
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]

    for i in range(1, n + 1): dp[1][i] = sum(arr[0: i])
    for i in range(1, k + 1): dp[i][1] = arr[0]
    for i in range(2, k + 1):  # 2 to n boards
        for j in range(2, n + 1):
            best = float('inf')
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p], sum(arr[p: j])))
            dp[i][j] = best

    return dp[k][n]


def solve_by_rec(arr, n, k):
    def find(n, k, best=float('inf'), qb=dict()):
        if k == 1: return sum(arr[:n])
        if n == 1: return arr[0]
        key = (n, k)
        if key in qb: return qb[key]
        for i in range(1, n):
            best = min(best, max(sum(arr[i: n]), find(i, k - 1)))
        qb[key] = best
        return qb[key]

    return find(n, k)


arr = [10, 20, 60, 50, 30, 40]
k = 3
arr = [10, 10, 10, 10]
k = 2
arr = [10, 20, 30, 40]
k = 2
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(solve_by_rec(arr, len(arr), k))

print(solve_by_tabulation(arr, len(arr), k))
