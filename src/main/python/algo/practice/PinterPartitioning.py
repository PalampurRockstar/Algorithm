def solve(arr, k):
    def find(n, k, best=float('inf')):
        if k == 1: return sum(arr[:n])
        if n == 1: return arr[0]
        for i in range(1, n): best = min(best, max(sum(arr[i:n]), find(i, k - 1)))

    return solve(len(arr), k)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(solve(arr, k))
