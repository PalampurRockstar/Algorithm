# https://leetcode.com/problems/prison-cells-after-n-days

def solve(arr, n):
    l = len(arr)
    found = {}
    visited = set()
    cell = arr
    for i in range(0, n + 1):
        cell = [0] + [1 if cell[j - 1] == cell[j + 1] else 0 for j in range(1, l - 1)] + [0]
        if str(cell) in visited:
            mod = (n % i) - 1
            return found[mod]
        found[i] = cell
        visited.add(str(cell))
    return cell


arr = [1, 0, 0, 1, 0, 0, 1, 0]
n = 1000000000

print(solve(arr, n))
