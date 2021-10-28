def solve(arr, n):
    i = 0
    t = i + 1
    while t < len(arr) and arr[t] < n:
        arr[t - 1] = arr[t]
        t += 1
    arr[t - 1] = n
    return arr


arr = [2, 4, 6, 8, 10]

print(solve(arr,3))
