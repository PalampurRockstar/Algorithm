# https://leetcode.com/problems/permutations

def solve(arr):
    res = []

    def find(found, n_a):
        if len(n_a) == 0:
            return res.append(found)
        for i, e in enumerate(n_a):
            find(found + [e], n_a[:i] + n_a[i + 1:])

    find([], arr)
    return res


arr = [1, 2, 3]

print(solve(arr))
