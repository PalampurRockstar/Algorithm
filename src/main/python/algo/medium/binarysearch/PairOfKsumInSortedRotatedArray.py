# https://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

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

    def find_item_pair(l, r):
        if l > r: return None
        if (arr[l] + arr[r]) == k:
            return arr[l], arr[r]
        elif (arr[l] + arr[r]) > k:
            return find_item_pair(l, r - 1)
        else:
            return find_item_pair(l + 1, r)

    pivot = find_pivot(0, len(arr) - 1)
    if pivot:
        l = -(len(arr) - pivot - 1)
        return find_item_pair(l, pivot)
    return None


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = 3
arr = [11, 15, 6, 8, 9, 10]
n = 16
print(find(arr, n))
