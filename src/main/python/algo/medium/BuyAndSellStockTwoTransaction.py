import sys


# Leet code tested
def find(arr, ltr=[], ttm=-sys.maxsize, min_c=sys.maxsize, max_c=-sys.maxsize, msp=-sys.maxsize):
    for v in arr:#left to right
        min_c = min(min_c, v)
        msp = max(msp, v - min_c)
        ltr.append(msp)

    msp = -sys.maxsize
    for i, v in reversed(list(enumerate(arr))): #right to left
        max_c = max(max_c, v)
        msp = max(msp, max_c - v)
        ttm = max(ttm, msp + ltr[i])
    return ttm


input = [7, 1, 5, 3, 6, 4]
input = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 20, 40, 45, 71, 50, 55]
input = [3, 3, 5, 0, 0, 3, 1, 4]
input = [1, 2, 3, 4, 5]
input = [7, 6, 4, 3, 1]
input = [1, 2]
print(find(input))
