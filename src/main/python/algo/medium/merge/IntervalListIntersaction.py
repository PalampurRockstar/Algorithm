def solve(first, second):
    arr = []

    def merge(f, s):
        nonlocal arr
        if f == len(first):
            return arr.extend(second[s:])
        if s == len(second):
            return arr.extend(first[f:])
        if first[f][0] < second[s][0]:
            arr.append(first[f])
            merge(f + 1, s)
        else:
            arr.append(second[s])
            merge(f, s + 1)

    merge(0, 0)
    print(arr)
    res = []
    for i in range(len(arr) - 1):
        low, high = max(arr[i][0], arr[i + 1][0]), min(arr[i][1], arr[i + 1][1])
        if low <= high: res.append([low, high])
        arr[i + 1][1] = max(arr[i][1], arr[i + 1][1])
    return res


first = [[0, 2], [5, 10], [13, 23], [24, 25]]
second = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(solve(first, second))
