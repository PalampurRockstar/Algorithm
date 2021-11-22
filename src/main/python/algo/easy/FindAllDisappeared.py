def solve(arr):
    l = len(arr)
    res = []
    t_sum = sum(arr)
    for i in range(l):
        index = arr[i] - 1
        if index > l:
            index = arr[i] - (l * 2) - 1
        print(index)
        if arr[index] > l:
            print(index + 1)
            res.append(index + 1)
        else:
            arr[index] += (l * 2)
    answer = []
    for i in range(l):
        if arr[i] <= l:
            answer.append(i + 1)
    return answer


arr = [4, 3, 2, 7, 8, 2, 3, 1]


def solve(arr):
    l = len(arr)
    for i in range(l):
        index = arr[i] - (l * 2) - 1 if arr[i] > l else arr[i] - 1
        if arr[index] <= l: arr[index] += l * 2
    res = []
    for i in range(l):
        if arr[i] <= l:
            res.append(i + 1)
    return res


print(solve(arr))
