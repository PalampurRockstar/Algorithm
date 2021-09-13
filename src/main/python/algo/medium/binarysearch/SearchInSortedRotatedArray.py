# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

def find(arr, k):
    def find_pivot(l, r):
        if arr[l] < arr[r] or l > r: return None
        if l == r: return l
        mid = int((l + r) / 2)
        if arr[mid] > arr[r]:
            if arr[mid] > arr[mid + 1]:
                return mid
            else:
                return find_pivot(mid + 1, r)
        else:
            if arr[mid - 1] > arr[mid]:
                return mid - 1
            else:
                return find_pivot(l, mid - 1)

    def find_item(l, r):
        if l > r: return None
        mid = int((l + r) / 2)
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return find_item(mid + 1, r)
        else:
            return find_item(l, mid - 1)

    pivot = find_pivot(0, len(arr) - 1)
    if pivot:
        if arr[0] < k < arr[pivot]:
            return find_item(0, pivot)
        else:
            return find_item(pivot + 1, len(arr) - 1)
    return find_item(0, len(arr) - 1)


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = 3
arr = [30, 32, 40, 50, 10, 20, 25, 28, 29]
n = 20
print(find(arr, n))
