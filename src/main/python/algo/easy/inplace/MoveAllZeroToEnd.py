# https://www.geeksforgeeks.org/move-zeroes-end-array/


def solve(arr):
    s, e = 0, len(arr) - 1
    while s < e:
        if arr[e] == 0:
            e -= 1
        elif arr[s] != 0:
            s += 1
        else:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
    return arr


def solution(arr):
    l = len(arr)
    zero = 0
    non_zero = 0
    while non_zero < l and zero < l:
        if arr[non_zero] == 0:
            non_zero += 1
        else:
            if non_zero != zero: arr[non_zero], arr[zero] = arr[zero], arr[non_zero]
            non_zero += 1
            zero += 1
    return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
# print(solve(arr))
# print(pushZerosToEnd(arr))
print(arr)
print(solution(arr))
