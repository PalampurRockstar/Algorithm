def find(arr):
    l = len(arr)
    ltr = [arr[0]]
    for i in arr[1:]:
        ltr.append(ltr[-1] + i)
    rtl = [0] * l
    acc = 0
    for i in reversed(range(l)):
        acc += arr[i]
        rtl[i] = acc
    for i in range(1, l - 1):
        left = i - 1
        right = i + 1
        if ltr[left] == rtl[right]:
            return i


def find(arr, acc=0):
    S = sum(arr)
    for i, v in enumerate(arr):
        if S - (v + acc) == acc:
            return i
        acc += v
    return -1


arr = [-7, 1, 5, 2, -4, 3, 0]
print(find(arr))
