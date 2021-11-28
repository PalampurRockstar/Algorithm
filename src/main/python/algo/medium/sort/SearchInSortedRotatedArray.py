# https://leetcode.com/problems/search-in-rotated-sorted-array/


def solve(arr, k):
    l = len(arr)

    def find(i, j):
        print(i, j)
        if -1 < i <= j < l:
            mid = (i + j) // 2
            print(mid)
            if arr[mid] == k:
                return mid
            if arr[i] <= arr[mid] <= arr[j]:
                if k < arr[mid]:
                    return find(i, mid - 1)
                else:
                    return find(mid + 1, j)
            elif arr[i] <= arr[mid]:
                if arr[i] <= k < arr[mid]:
                    return find(i, mid - 1)
                else:
                    return find(mid + 1, j)
            else:
                if arr[mid] < k <= arr[j]:
                    return find(mid + 1, j)
                else:
                    return find(i, mid - 1)
        else:
            return -1

    return find(0, l - 1)


arr = [4, 5, 6, 7, 0, 1, 2]
k = 0
print(solve(arr, k))
