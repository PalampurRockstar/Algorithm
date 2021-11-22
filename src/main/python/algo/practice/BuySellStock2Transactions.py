import sys


def solve(arr):
    ltr = [0]
    min_so_far = arr[0]
    for each in arr[1:]:
        ltr.append(max(ltr[-1], each - min_so_far))
        min_so_far = min(min_so_far, each)
    max_so_far = arr[-1]
    max_gain_so_far = 0
    rtl = [0] * len(arr)
    index = len(arr) - 2
    while index >= 0:
        rtl[index] = max(max_gain_so_far, max_so_far - arr[index])
        max_gain_so_far = rtl[index]
        max_so_far = max(max_so_far, arr[index])
        index -= 1
    return max([right + left for right, left in zip(rtl, ltr)])


arr = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 20, 40, 45, 71, 50, 55]
arr = [2, 30, 15, 10, 8, 25, 80]
arr = [90, 80, 70, 60, 50]
print(solve(arr))
