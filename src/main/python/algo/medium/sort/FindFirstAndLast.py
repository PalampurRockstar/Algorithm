# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

def solve(arr, k):
    l = len(arr)

    def find(i, j, direction=None):
        if -1 < i <= j < l:
            mid = (i + j) // 2
            if arr[mid] == k and not direction:
                left_r = find(i, mid - 1, 'left')
                right_r = find(mid + 1, j, 'right')
                return left_r if -1 != left_r else mid, right_r if -1 != right_r else mid
            elif arr[mid] == k and direction:
                if direction == 'right':
                    right_r = find(mid + 1, j, direction)
                    return right_r if right_r != -1 else mid
                else:
                    left_r = find(i, mid - 1, direction)
                    return left_r if left_r != -1 else mid
            elif k < arr[mid]:
                return find(i, mid - 1, direction)
            else:
                return find(mid + 1, j, direction)
        else:
            return -1 if direction else (-1, -1)

    return find(0, l - 1)


arr = [5, 7, 7, 8, 8, 10]
k = 8
print(solve(arr, k))
