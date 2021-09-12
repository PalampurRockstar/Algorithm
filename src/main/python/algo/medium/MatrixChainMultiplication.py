import sys


def bottom_up(arr):

    new_arr = [[arr[i], arr[i + 1]] for i in range(len(arr) - 1)]
    new_l = len(new_arr)
    dp = [[0 for _ in range(new_l)] for _ in range(new_l)]
    for g in range(len(new_arr)):
        for j in range(g, new_l):
            i = j - g
            if g == 0:
                dp[i][j] = 0
            elif g == 1:
                dp[i][j] = new_arr[i][0] * new_arr[i][1] * new_arr[j][1]
            else:
                dp[i][j] = sys.maxsize
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + (new_arr[i][0] * new_arr[k][1] * new_arr[j][1]))
    return dp[0][len(dp) - 1]


def top_down_1_wrap(arr):
    return top_down_1(arr, 0, len(arr) - 2, dict())


def top_down_2_wrap(arr):
    return top_down_2(arr, 1, len(arr) - 1)


def top_down_1(arr, left, right, qb):
    if left == right: return 0
    key = str(left) + ":" + str(right)
    if key in qb: return qb[key]
    qb[key] = sys.maxsize
    for k in range(left, right):
        qb[key] = min(qb[key], top_down_1(arr, left, k, qb) + top_down_1(arr, k + 1, right, qb) +
                      (arr[left] * arr[right + 1] * arr[k + 1]))
    return qb[key]


def top_down_2(arr, i, j):
    if i == j:
        return 0
    M = sys.maxsize
    for k in range(i, j):
        M = min(M, top_down_2(arr, i, k) + top_down_2(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j])
    return M


arr = [4, 2, 3, 1, 3]
arr = [1, 2, 3, 4, 3]
arr = [1, 2, 3, 4]
arr = [1, 2, 3]

print(bottom_up(arr))
print(top_down_1_wrap(arr))
print(top_down_2_wrap(arr))
