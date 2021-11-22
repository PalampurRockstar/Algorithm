from collections import defaultdict


def solve(arr, k):
    div_map = defaultdict(int)
    acc = 0
    div_map[acc] = 1
    res = 0
    for each in arr:
        acc += each
        if acc % k in div_map:
            res += div_map[acc % k]
        div_map[acc % k] += 1

    return res


arr = [4, 5, 0, -2, -3, 1]
k = 5

arr = [2, 7, 6, 1, 4, 5]
k = 3
print(solve(arr, k))
