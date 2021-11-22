# https://leetcode.com/problems/trapping-rain-water/

def solve_right_left(arr):
    max_at_left = arr[0:1]
    for v in arr[1:]:
        max_at_left.append(max(max_at_left[-1], v))

    max_at_right = [float('-inf')] * len(arr)
    MAX = float('-inf')
    for i, v in reversed(list(enumerate(arr))):
        MAX = max(MAX, v)
        max_at_right[i] = (MAX)
    react = 0
    for l, r, v in zip(max_at_right, max_at_left, arr):
        react += min(l, r) - v
    return react


def solve_simple(arr):
    right = len(arr) - 1
    left = 0
    right_max = arr[right]
    left_max = arr[left]
    res = 0
    while right > left:
        if arr[right] < arr[left]:
            right_max = max(right_max, arr[right])
            res += right_max - arr[right]
            right -= 1
        else:
            left_max = max(left_max, arr[left])
            res += left_max - arr[left]
            left += 1
    return res


def solve_using_stack(arr, S=[], res=0):
    for i, v in enumerate(arr):
        while S and arr[S[-1]] <= v:
            pop = S.pop()
            if S: res += (min(arr[S[-1]], arr[i]) - arr[pop]) * (i - (S[-1] + 1))
        S.append(i)
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solve_using_stack(arr))
