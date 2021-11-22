# https://www.geeksforgeeks.org/chocolate-distribution-problem
import collections


def solve(arr, k):
    window = collections.deque([])
    arr = sorted(arr)
    min_most = float('inf')
    for i in range(len(arr)):
        if len(window) == k:
            min_most = min(min_most, window[-1] - window[0])
            window.append(arr[i])
            window.popleft()
        else:
            window.append(arr[i])
    return min_most


arr = [7, 3, 2, 4, 9, 12, 56]
k = 3

arr = [3, 4, 1, 9, 56, 7, 9, 12]
k = 5
print(solve(arr, k))
