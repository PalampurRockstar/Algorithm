import math


def solve(arr, k):
    M = 0
    for v in arr:
        if M < k:
            M += v
        else:
            break
    res = M - k
    return int(math.sqrt(res ** 2))


arr = [6, 1, 2, 1]
k = 100
print(solve(arr, k))
