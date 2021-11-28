# https://leetcode.com/problems/all-paths-from-source-to-target/
def solve(arr):
    res = []
    l = len(arr)

    def find(found, index):
        if index == l - 1: return res.append(found)
        for each in arr[index]:
            find(found + [each], each)

    find([0], 0)
    return res


arr = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print(solve(arr))
