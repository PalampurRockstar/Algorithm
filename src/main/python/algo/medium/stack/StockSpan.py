def find(arr, res=[], stack=[]):
    for v in arr:
        sm = 1
        while stack and stack[-1][0] < v: sm += stack.pop()[1]
        res.append(sm)
        stack.append([v, sm])
    return res


arr = [100, 80, 60, 70, 60, 75, 85]
print(find(arr))
