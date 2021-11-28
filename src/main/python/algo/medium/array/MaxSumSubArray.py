# https://leetcode.com/problems/maximum-subarray/
def solve(arr):
    t_m = float('-inf')
    c_m = 0
    for v in arr:
        if c_m + v < v:
            c_m = v
        else:
            c_m += v
        t_m = max(c_m, t_m)
    return t_m


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(solve(arr))
