def solve(arr):
    length = len(arr)
    DP = [0] * length
    for i in range(length):
        MAX = 0
        for j in range(i):
            if arr[i] > arr[j]:
                MAX = max(MAX, DP[j])
        DP[i] = MAX + 1
    print(DP)
    return max(DP)


arr = [3, 10, 2, 1, 20]
print(solve(arr))
