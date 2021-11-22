# https://www.geeksforgeeks.org/minimize-the-maximum-difference-between-the-heights/

def solve(arr, k):
    l = len(arr)
    if (l == 1):
        return 0
    arr.sort()
    ans = arr[l - 1] - arr[0]
    small = arr[0] + k
    big = arr[l - 1] - k
    if small > big:
        small, big = big, small
    for each in arr[1:-1]:
        subtract = each - k
        add = each + k
        if small <= subtract or add <= big:
            continue
        if add - big <= small - subtract:
            big = add
        else:
            small = subtract
    return min(ans, big - small)


arr = [1, 15, 10]
k = 6

arr = [1, 10, 14, 14, 14, 15]
k = 6

arr = [1, 15, 10]
k = 6

arr = [1, 5, 15, 10]
k = 3

arr = [6, 10]
k = 3

arr = [1, 10, 14, 14, 14, 15]
k = 6

arr = [1, 2, 3]
k = 2
print(solve(arr, k))
