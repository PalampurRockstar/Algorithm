import sys


def find(arr, ltr=[], ttm=-sys.maxsize, min_c=sys.maxsize, max_c=-sys.maxsize, msp=-sys.maxsize):
    for v in arr:
        min_c = min(min_c, v)
        msp = max(msp, v - min_c)
        ltr.append(msp)
    msp = -sys.maxsize

    for i, v in reversed(list(enumerate(arr))):
        max_c = max(max_c, v)
        msp = max(msp, max_c - v)
        ttm = max(ttm, msp + ltr[i])
    return ttm


arr = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 20, 40, 45, 71, 50, 55]

print(find(arr))
