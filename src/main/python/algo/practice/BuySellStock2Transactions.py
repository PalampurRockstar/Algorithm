# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

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


# test cases

assert solve([3, 3, 5, 0, 0, 3, 1, 4]) == 6
assert solve([1, 2, 3, 4, 5]) == 4
assert solve([7, 6, 4, 3, 1]) == 0
assert solve([2, 30, 15, 10, 8, 25, 80]) == 100
