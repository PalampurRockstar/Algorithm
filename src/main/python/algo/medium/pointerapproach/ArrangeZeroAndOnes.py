# https://leetcode.com/problems/ones-and-zeroes/
def solve(arr):
    length = len(arr)
    zero = 0
    two = length - 1
    one = 0
    while zero <= one <= two:
        if arr[one] == 0:
            arr[one], arr[zero] = arr[zero], arr[one]
            zero += 1
        elif arr[one] == 2:
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1
        if arr[one] == 1:
            one += 1
        one = max(one, zero + 1)
    return arr


def solve_rec(arr):
    length = len(arr)

    def find(s, e):
        mid = s + 1
        while s <= mid <= e:
            if arr[mid] == 0:
                arr[mid], arr[s], arr[s], arr[mid]
                return find(s + 1, e)
            elif arr[s + 1] == 2:
                arr[mid], arr[e], arr[e], arr[mid]
                return find(s, e + 1)
            else:
                mid += 1

    find(0, length - 1)
    return arr


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# arr = [0, 1, 2, 2, 0, 0]

print(solve(arr))
print(solve_rec(arr))
