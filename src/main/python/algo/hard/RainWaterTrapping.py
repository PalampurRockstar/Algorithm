import sys


def find(arr):
    l = len(arr)
    rtl = [0] * l
    M = -sys.maxsize
    for i, v in reversed(list(enumerate(arr))):
        M = max(M, v)
        rtl[i] = M
    print(rtl)
    ltr = [arr[0]]
    res = 0
    for i, v in enumerate(arr[1:], 1):
        ltr.append(max(v, ltr[-1]))
        if not (v == ltr[i] or v == rtl[i]):
            res += min(ltr[i], rtl[i]) - v
    return res


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(find(arr))
