import collections
import sys


# leet code tested

def find(arr):
    arr.append(0)
    area = 0
    S = []
    for i, v in enumerate(arr):
        while S and arr[S[-1]] >= v:
            x = S.pop()
            if S:
                area = max(area, arr[x] * (i - S[-1] - 1))
            else:
                area = max(area, arr[x] * i)
        S.append(i)
    return area


def convert(arr):
    height = max(arr)
    return [[0 if i < (height - j) else 1 for j in arr] for i in range(height)]


# result=10
arr = [2, 1, 5, 6, 2, 3]
# result=4
# arr = [2, 4]

print(find(arr))
