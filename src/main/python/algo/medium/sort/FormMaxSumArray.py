# https://leetcode.com/problems/largest-number
from functools import cmp_to_key


def solve(num):
    compare = lambda a, b: -1 if a + b > b + a else 1 if a + b < b + a else 0
    num = [str(i) for i in num]
    return "".join(sorted(num, key=cmp_to_key(compare)))


arr = [3, 30, 34, 5, 9]
print(solve(arr))
