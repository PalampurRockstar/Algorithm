import collections


def solve(arr):
    STACK = collections.deque([])
    for each in arr:
        while STACK and len(STACK) > 2: STACK.popleft()
        if STACK:
            if STACK[-1] < each:
                STACK.append(each)
            else:
                STACK[0] = max(STACK[0], each)
        else:
            STACK.append(each)
    return STACK[-1], STACK[-2]


def solve_two(arr):
    first = float('-inf')
    second = float('-inf')
    for each in arr:
        if each > first:
            second = first
            first = each
        elif each > second and each != first:
            second = each

    return first, second


arr = [12, 35, 1, 10, 34, 1]
print(solve(arr))
print(solve_two(arr))
