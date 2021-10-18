# https://leetcode.com/problems/largest-number/

import sys


def solve(nums):
    if len(nums) == 0: return ""

    def parse(a, b):
        return int(str(a) + str(b))

    def find(arr, pi=0):
        if len(arr) == 0: return ""
        n = arr[0]
        M = n
        n_arr = arr[1:]
        for i, v in enumerate(n_arr):
            if parse(v, n) > M or parse(n, v) > M:
                pi = i
                M = max(parse(v, n), parse(n, v))

        r = find(n_arr[1:pi] + n_arr[pi + 1:])
        return max(parse(M, r), parse(r, M))

    return str(find(nums))


# arr = [10, 2]
# print(solve(arr))

arr = [3, 30, 34, 5, 9]
print(solve(arr))
