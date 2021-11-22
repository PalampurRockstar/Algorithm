arr = [[1, 4, 5], [1, 3, 4], [2, 6]]


def solve(arr):
    res = []
    max_len = max([len(v) for v in arr])
    for i in range(max_len):
        print(sorted(arr[:, 1:]))
        res += sorted(arr[:][i])
    return res


print(solve(arr))
