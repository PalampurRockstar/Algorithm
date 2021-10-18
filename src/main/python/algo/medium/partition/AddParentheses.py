#https://leetcode.com/problems/different-ways-to-add-parentheses

def solve(arr):
    qb = dict()

    def find(s, e, res=[]):
        nonlocal qb
        key = str(s) + ":" + str(e)
        if key in qb: return qb[key]
        if e == s: return [arr[e]]
        for i in range(s, e - 1, 2):
            op = arr[i + 1]
            for ot in find(s, i):
                for inn in find(i + 2, e):
                    res.append(s_to_o(ot, op, inn))
        qb[key] = res
        return qb[key]

    def s_to_o(a, o, b):
        a = int(a)
        b = int(b)
        op = {
            '-': lambda: a - b,
            '+': lambda: a + b,
            '*': lambda: a * b,
            '/': lambda: a / b
        }
        return op[o]()

    return find(0, len(arr) - 1)


arr = "2-1-1"
print(solve(arr))

arr = "2*3-4*5"
print(solve(arr))
