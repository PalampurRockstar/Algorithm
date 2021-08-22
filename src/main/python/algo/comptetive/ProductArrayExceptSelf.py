def find(arr):
    l = len(arr)
    if l == 0: return 0
    if l == 1: return arr[0]
    ltr = [arr[i] if i == 0 else 1 for i in range(l)]
    for i, v in enumerate(arr[1:], 1):
        ltr[i] = ltr[i - 1] * v
    rtl = [arr[i] if i == l - 1 else 1 for i in range(l)]
    for i, v in reversed(list(enumerate(arr[:-1]))):
        rtl[i] = rtl[i + 1] * v
    res = []
    for i in range(l):
        if i == 0:
            res.append(rtl[i + 1])
        elif i == l - 1:
            res.append(ltr[i - 1])
        else:
            res.append(ltr[i - 1] * rtl[i + 1])
    return res


def find_on_fly(arr):
    l = len(arr)
    if l == 0: return 0
    if l == 1: return arr[0]
    ltr = [arr[0]]
    for v in arr[1:]:
        ltr.append(ltr[- 1] * v)
    acc_rtl = 1
    for i in reversed(range(l)):
        if i == 0:
            ltr[i] = acc_rtl
        elif i == l - 1:
            ltr[i] = ltr[i - 1]
        else:
            ltr[i] = acc_rtl * ltr[i - 1]
        acc_rtl *= arr[i]
    return ltr


arr = [10, 3, 5, 6, 2]
print(find(arr))
print(find_on_fly(arr))
