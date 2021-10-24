def rotate(arr, k):
    l = len(arr)
    k = k % l
    if k < 0: k += l

    def reverse(s, e):
        while e > s:
            arr[e], arr[s] = arr[s], arr[e]
            e -= 1
            s += 1

    reverse(0, l - k - 1)
    reverse(l - k, l - 1)
    reverse(0, l - 1)
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = -7
print(rotate(arr, k))
