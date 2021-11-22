# https://leetcode.com/problems/first-missing-positive

def solve(arr):
    l = len(arr)
    for i in range(l):
        if arr[i] > l or arr[i] <= 0: arr[i] = l + 1
    for i in range(l):
        index = abs(arr[i]) - 1
        if index < l: arr[index] = -abs(arr[index])

    for i in range(l + 1):
        if i == l or arr[i] >= 0:
            return i + 1
    return -1


arr = [7, 8, 9, 11, 12]
arr = [1, 2, 0]
# arr = [3, 4, -1, 1]
# arr = [1]
# arr = [0, 1, 2]
print(solve(arr))
