# https://www.geeksforgeeks.org/find-k-pairs-smallest-sums-two-arrays/
def find(arr1, arr2, k):
    res = []

    def solve(i1=0, i2=0):
        if k == len(res): return
        if i1 < len(arr1) and i2 < len(arr2):
            res.append((arr1[i1], arr2[i2]))
        if i1 + 1 < len(arr1) and i2 + 1 < len(arr2):
            if arr1[i1 + 1] > arr2[i2 + 1]:
                solve(i1, i2 + 1)
            else:
                solve(i1 + 1, i2)

    solve()
    return res


arr1 = [1, 7, 11]
arr2 = [2, 4, 6]
print(find(arr1, arr2, 3))
