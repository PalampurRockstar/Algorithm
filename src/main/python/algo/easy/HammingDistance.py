# https://leetcode.com/problems/hamming-distance

def solve(x, y):
    x = str(bin(x)).replace("b", "")
    y = str(bin(y)).replace("b", "")
    if len(x) > len(y):
        y = ("0" * (len(x) - len(y))) + y
    else:
        x = ("0" * (len(y) - len(x))) + x
    return ([int(i) ^ int(j) for i, j in zip(x, y)]).count(True)


def solve_by(x, y):
    xor = x ^ y
    res = 0
    while xor != 0:
        if xor & 1: res += 1
        xor = xor >> 1
    return res


x = 1
y = 4
print(solve(x, y))
print(solve_by(x, y))
