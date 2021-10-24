def solve(arr):
    l = len(arr)
    T = [1] * l
    for i in range(1, l):
        M = 0
        for k in range(i):
            if arr[i] > arr[k]:
                M = max(M, T[k])
        T[i] += M
    print(T)
    return max(T)


arr = [3, 10, 2, 1, 20]
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(solve(arr))
