# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/


def solve(arr, stg=True):
    for i, v in enumerate(arr[1:], 1):
        if stg:
            if arr[i - 1] > v:
                arr[i], arr[i - 1] = arr[i - 1], v
        else:
            if arr[i - 1] < v:
                arr[i], arr[i - 1] = arr[i - 1], v
        stg = not stg
    return arr


arr = [4, 3, 7, 8, 6, 2, 1]
print(solve(arr))

arr = [1, 4, 3, 2]
print(solve(arr))