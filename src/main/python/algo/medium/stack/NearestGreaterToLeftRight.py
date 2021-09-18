def find_left_next_greater(arr):
    stack = []
    res = []
    for v in arr:
        while stack and stack[-1] < v: stack.pop()
        res.append(-1 if not stack else stack[-1])
        stack.append(v)
    return res


def find_right_next_greater(arr):
    stack = []
    res = []
    for v in arr[::-1]:
        while stack and stack[-1] < v: stack.pop()
        res.append(-1 if not stack else stack[-1])
        stack.append(v)
    return res[::-1]


arr = [13, 7, 6, 12]

print(find_left_next_greater(arr))
print(find_right_next_greater(arr))
