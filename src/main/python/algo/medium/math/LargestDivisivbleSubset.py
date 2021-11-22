def solve(arr):
    arr = sorted(arr)
    l = len(arr)
    DP = [[1, i] for i in range(l)]
    res = float('-inf')
    res_index = -1
    for i in range(l):
        MAX = 0
        index = -1
        for j in range(i):
            if arr[i] % arr[j] == 0:
                if MAX < DP[j][0]:
                    MAX = DP[j][0]
                    index = j
        DP[i][0] += MAX
        DP[i][1] = index

        if res < DP[i][0]:
            res_index = i
            res = DP[i][0]
    answer = []
    while -1 < res_index < l:
        answer.append(arr[res_index])
        res_index = DP[res_index][1]
    return answer


def solve(arr):
    arr = sorted(arr)
    l = len(arr)
    DP = [1] * l
    res = float('-inf')
    for i in range(l):
        c_max = 0
        for j in range(i):
            if arr[i] % arr[j] == 0:
                c_max = max(c_max, DP[j])
        DP[i] += c_max
        res = max(res, DP[i])
    return res


arr = [1, 2, 3]
arr = [1, 2, 4, 8]

print(solve(arr))
