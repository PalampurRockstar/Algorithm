# https://leetcode.com/problems/triangle/


def solve(arr):
    external_length = len(arr)
    for i in range(external_length):
        internal_length = len(arr[i])
        for j in range(internal_length):
            if i != 0:
                if j == 0:
                    arr[i][j] += arr[i - 1][j]
                elif j == internal_length - 1:
                    arr[i][j] += arr[i - 1][j - 1]
                else:
                    arr[i][j] += min(arr[i - 1][j], arr[i - 1][j - 1])
    print(arr)
    return min(arr[len(arr) - 1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(triangle)
print(solve(triangle))
