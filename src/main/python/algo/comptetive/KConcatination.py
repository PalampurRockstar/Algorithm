import sys


def find(arr, k, cm=-sys.maxsize, tm=-sys.maxsize):
    new_arr = [*arr] * k
    for i in new_arr:
        cm = max(cm + i, i)
        tm = max(tm, cm)
    return tm



print(find([1, -2, 1], 2))


