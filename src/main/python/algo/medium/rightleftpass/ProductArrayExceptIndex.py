def solve(arr):
    left_to_right = [arr[0]]
    for e in arr[1:]:
        left_to_right.append(left_to_right[-1] * e)
    right_to_left = [arr[-1]]
    for e in reversed(arr[:-1]):
        right_to_left.append(right_to_left[-1] * e)
    right_to_left = list(reversed(right_to_left))
    answer = []
    for i in range(len(arr)):
        if -1 < i - 1 and i + 1 < len(arr):
            answer.append(left_to_right[i - 1] * right_to_left[i + 1])
        elif -1 < i - 1:
            answer.append(left_to_right[i - 1])
        elif i + 1 < len(arr):
            answer.append(right_to_left[i + 1])
    return answer


arr = [1, 2, 3, 4]
arr = [0, 0]
print(solve(arr))
