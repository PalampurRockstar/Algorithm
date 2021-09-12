#https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/
def find_by_rec(arr):
    if len(arr) == 0: return 0
    res = []

    def solve(index=1, g=True, prev=arr[0]):
        if index == len(arr):
            res.append(prev)
            return
        condition = prev < arr[index] if g else prev > arr[index]
        if condition:
            res.append(prev)
            prev = arr[index]
        else:
            res.append(arr[index])
        solve(index + 1, not g, prev)

    solve()
    return res


def find_by_inplace(arr):
    g = True
    for i in range(len(arr) - 1):
        if g:
            if arr[i] > arr[i + 1]: arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if arr[i] < arr[i + 1]: arr[i], arr[i + 1] = arr[i + 1], arr[i]
        g=not g
    return arr


arr = [4, 3, 7, 8, 6, 2, 1]
print(find_by_rec(arr))
print(find_by_inplace(arr))
