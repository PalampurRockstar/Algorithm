import collections


def find(arr):
    length = len(arr)
    jsr = [0] * length
    S = collections.deque([length])
    for i, v in reversed(list(enumerate(arr))):
        while S and S[-1] < length and v <= arr[S[-1]]: S.pop()
        jsr[i] = S[-1]
        S.append(i)
    return jsr

arr = [2, 1, 5, 6, 2, 3]
print(find(arr))
