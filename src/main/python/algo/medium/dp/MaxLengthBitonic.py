def solve(arr):
    l = len(arr)
    T_MAX, C_MAX = 1, 1
    T_MIN, C_MIN = 1, 1
    for i in range(1, l):
        if arr[i - 1] < arr[i]:
            C_MAX += 1
            C_MIN = 1
        else:
            C_MIN += 1
            C_MAX = 1
        T_MAX = max(T_MAX, C_MAX)
        T_MIN = max(T_MIN, C_MIN)
    return max(T_MAX,T_MIN)


arr = [12, 4, 78, 90, 45, 23]
print(solve(arr))
