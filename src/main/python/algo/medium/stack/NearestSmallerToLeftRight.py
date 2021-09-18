def find_right_next_smaller(arr):
    stack = []
    res = []
    for v in arr[::-1]:
        while stack and stack[-1] > v: stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(v)
    return res[::-1]


def find_left_next_smaller(arr):
    stack = []
    res = []
    for v in arr:
        while stack and stack[-1] > v: stack.pop()
        res.append(stack[-1] if stack else -1)
        stack.append(v)
    return res


arr = [13, 7, 6, 12]

print(find_right_next_smaller(arr))
print(find_left_next_smaller(arr))
