# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

def solve(arr, x):
    M = float('inf')
    dp = set()

    def find(i, j, x):
        if x < 0: return
        nonlocal M
        key = (i, j)
        if key in dp: return
        if -1 < i <= j and -1 < j < len(arr):
            if x == 0: M = min(M, len(arr) - ((j - i) + 1))
            find(i, j - 1, x - arr[j])
            find(i + 1, j, x - arr[i])
        # dp.add(key)

    find(0, len(arr) - 1, x)
    return M if M != float('inf') else -1


arr = [3, 2, 20, 1, 1, 3]
x = 10
print(solve(arr, x))
