import sys


def find(arr, dep):
    def is_intersection(f, s):
        if s < f:
            return True
        else:
            return False

    count = 1
    M = -sys.maxsize
    for i in range(len(arr) - 1):
        if is_intersection(dep[i] > arr[i + 1]):
            count += 1
            M = max(M, count)
        else:
            count = 1
    return M


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(find(arr, dep))
