def find_pivot(arr, l, r):
    if arr[l] < arr[r] or l > r: return None
    if l == r: return l
    mid = int((l + r) / 2)
    if arr[mid] > arr[r]:
        if arr[mid] > arr[mid + 1]:
            return mid
        else:
            return find_pivot(arr, mid + 1, r)
    else:
        if arr[mid - 1] > arr[mid]:
            return mid - 1
        else:
            return find_pivot(arr, l, mid - 1)


arr = [30, 32, 40, 50, 10, 20, 25, 28, 29]
arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
print(find_pivot(arr, 0, len(arr) - 1))
