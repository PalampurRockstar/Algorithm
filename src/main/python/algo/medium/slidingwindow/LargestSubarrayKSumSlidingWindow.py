#https://leetcode.com/problems/subarray-sum-equals-k/

import sys


def find(arr, k, b=0):
    M = -sys.maxsize
    win_max = 0
    for f, v in enumerate(arr):
        win_max += v
        while win_max > k:
            win_max -= arr[b]
            b += 1
        if win_max == k: M = max(M, (f - b) + 1)
    return M


arr = [10, 5, 2, 7, 1, 9]
k = 15

# arr = [4, 1, 1, 1, 2, 3, 5]
# k = 5
print(find(arr, k))
