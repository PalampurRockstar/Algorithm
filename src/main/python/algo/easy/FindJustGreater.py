# https://leetcode.com/problems/search-insert-position/


def solve(arr, k):
    l = len(arr)

    def find(i, j):
        if -1 < i <= j < len(arr):
            mid = (i + j) // 2
            if arr[mid] == k:
                return mid
            if arr[mid] < k:
                if mid + 1 < l and k < arr[mid + 1]:
                    return mid + 1
                elif mid + 1 >= l:
                    return mid + 1
                else:
                    return find(mid + 1, j)
            else:
                if -1 < mid - 1 and arr[mid - 1] < k:
                    return mid
                elif mid - 1 < 0:
                    return mid
                else:
                    return find(i, mid - 1)
        else:
            return -1

    return find(0, l - 1)


arr, k = [1, 3, 5, 6], 5

arr, k = [1, 3, 5, 6], 2

arr, k = [1, 3, 5, 6], 7
print(solve(arr, k))
