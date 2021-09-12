import math


def find(n):
    l = [True] * (n + 1)
    p = 2
    while (p * p) <= n:
        if l[p]:
            for j in range(p * p, n + 1, p):
                l[j] = False
        p += 1
    res = []
    for p in range(2, n + 1):
        if l[p]:
            res.append(p)
    return res


print(find(10))
