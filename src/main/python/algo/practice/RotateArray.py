def solve(arr, k):
    length = len(arr)
    k = k % length
    if k < 0: k = length - k

    def reverse(start, end):
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            reverse(start + 1, end - 1)

    k = (length - k)
    reverse(0, k - 1)
    reverse(k, length - 1)
    reverse(0, length - 1)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(solve(arr, k))
