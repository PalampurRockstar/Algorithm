#https://leetcode.com/problems/subarray-sum-equals-k/
import sys


def find(arr, k, acc=0):
    acc_map = {0: 0}
    M = -sys.maxsize
    for i, v in enumerate(arr, 1):
        acc += v
        acc_map[acc] = i
        if acc - k in acc_map:
            M = max(M, i - acc_map[acc - k])
    return M


arr = [10, 5, 2, 7, 1, 9]
k = 15

arr = [4, 1, 1, 1, 2, 3, 5]

k = 5
print(find(arr, k))
