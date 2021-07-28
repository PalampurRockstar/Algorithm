import collections


def find(arr):
    length = len(arr)
    jsl = [0] * length
    S = collections.deque([-1])
    for i, v in enumerate(arr):
        while S and S[-1] > -1 and v <= arr[S[-1]]: S.pop()
        jsl[i] = S[-1]
        S.append(i)
    return jsl


arr = [2, 1, 5, 6, 2, 3]
print(find(arr))
