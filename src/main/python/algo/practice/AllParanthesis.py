arr = "2*3-4*5"


def solve(arr):
    length = len(arr)
    if length == 1: return arr[0]

    def find(start, end):
        res = []
        print(start, end)
        if start == end: return [arr[start]]
        for i in range(start + 1, end, 2):
            for f in find(start, i - 1):
                for l in find(i + 1, end):
                    res.append(operation(f, arr[i], l))
        return res

    def operation(a, operand, b):
        print(a, operand, b)
        a = int(a)
        b = int(b)
        OP = {
            '/': lambda: a // b,
            '*': lambda: a * b,
            '-': lambda: a - b,
            '+': lambda: a + b
        }
        res = OP[operand]()
        return res

    return find(0, length - 1)


arr = "2*3-4*5"
print(solve(arr))
