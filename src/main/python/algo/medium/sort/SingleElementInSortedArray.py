# https://leetcode.com/problems/single-element-in-a-sorted-array/
def solve(arr):
    def find(i, j):
        if -1 < i <= j < len(arr):
            if i == j: return arr[i]
            mid = (i + j) // 2
            if mid == 0 and arr[mid] != arr[mid + 1]: return arr[mid]
            if mid == len(arr) - 1 and arr[mid - 1] != arr[mid]: return arr[mid]
            if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]: return arr[mid]
            if mid % 2 == 0:
                if arr[mid] == arr[mid + 1]:
                    return find(mid + 1, j)
                else:
                    return find(i, mid - 1)
            else:
                if arr[mid] == arr[mid + 1]:
                    return find(i, mid - 1)
                else:
                    return find(mid + 1, j)
        else:
            return None

    return find(0, len(arr) - 1)


arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
# arr = [3, 3, 7, 7, 10, 11, 11]
print(solve(arr))
