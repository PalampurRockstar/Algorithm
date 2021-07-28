import collections
import sys


# leet code tested
def findUsingTwoArray(arr):
    length = len(arr)
    S = collections.deque([-1])
    jsl = [0] * length
    for i, v in enumerate(arr):
        while S and S[-1] > -1 and v <= arr[S[-1]]: S.pop()
        jsl[i] = S[-1]
        S.append(i)
    S = collections.deque([length])
    jsr = [0] * length
    for i, v in reversed(list(enumerate(arr))):
        while S and S[-1] < length and v <= arr[S[-1]]: S.pop()
        jsr[i] = S[-1]
        S.append(i)
    tm = -sys.maxsize
    for i, v in enumerate(arr):
        tm = max(tm, (jsr[i] - jsl[i] - 1) * v)
    return tm if tm != -sys.maxsize else 0


def findUsingStackArray(arr):
    arr.append(0)
    area = -sys.maxsize
    S = []
    for i, v in enumerate(arr):
        while S and arr[S[-1]] >= v:
            ri = S.pop()  # removed index
            width = i - S[-1] - 1 if S else i
            area = max(area, arr[ri] * width)
        S.append(i)
    return area


# result=10
arr = [2, 1, 5, 6, 2, 3]
arr = [2, 1, 5, 6, 1, 3]
print(findUsingTwoArray(arr))
print(findUsingStackArray(arr))
