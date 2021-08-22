import sys


def find(arr):
    c_max = t_max = -sys.maxsize
    c_min = t_min = sys.maxsize
    for i in arr:
        c_max = max(c_max + i, i)
        t_max = max(c_max, t_max)
        c_min = min(c_min + i, i)
        t_min = min(c_min, t_min)
    S = sum(arr)
    if S == t_min: return t_max
    return max(S - t_min, t_max)


print(find([11, 10, -20, 5, -3, -5, 8, -13, 10]))
