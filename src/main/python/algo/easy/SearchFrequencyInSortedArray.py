def solve(arr, k):
    l = len(arr)

    def first_occurance(s, e):
        if e < s:
            return -1
        else:
            mid = (e + s) // 2
            if mid - 1 > -1 and arr[mid] == k and arr[mid - 1] == k or k < arr[mid]:
                return first_occurance(s, mid - 1)
            elif arr[mid] == k:
                return mid
            else:
                return first_occurance(mid + 1, e)

    def last_occurance(s, e):
        if e < s:
            return -1
        else:
            mid = (e + s) // 2
            if mid + 1 < l and arr[mid] == k and arr[mid + 1] == k or k > arr[mid]:
                return last_occurance(mid + 1, e)
            elif arr[mid] == k:
                return mid
            else:
                return last_occurance(s, mid - 1)

    first = first_occurance(0, l - 1)
    last = last_occurance(0, l - 1)
    print(first, end="\t")
    print(last)
    return last - first + 1 if first != -1 else 0


# arr = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
# print(solve(arr, 9))

arr = [1, 1, 2]
print(solve(arr, 1))
