def solve(arr):
    def find(s, e):
        if -1 < s <= e and -1 < e < len(arr):
            mid = (s + e) // 2
            if mid % 2 != 0:
                if mid - 1 > -1 and arr[mid - 1] == arr[mid]:
                    return find(mid + 1, e)
                elif mid + 1 >= len(arr) or arr[mid] != arr[mid + 1]:
                    return arr[mid]
                else:
                    return find(s, mid - 1)
            else:
                if mid + 1 < len(arr) and arr[mid] == arr[mid + 1]:
                    return find(mid + 1, e)
                elif mid - 1 < 0 or arr[mid - 1] != arr[mid]:
                    return arr[mid]
                else:
                    return find(s, mid - 1)
        else:
            return -1

    return find(0, len(arr) - 1)


arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(solve(arr))
