# https://leetcode.com/problems/container-with-most-water

def solve(arr):
    left = 0
    right = len(arr) - 1
    res = 0
    while left < right:
        width = (right - left)
        if arr[left] < arr[right]:
            res = max(res, arr[left] * width)
            left += 1
        else:
            res = max(res, arr[right] * width)
            right -= 1
    return res


arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solve(arr))
