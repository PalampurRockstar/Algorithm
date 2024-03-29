def solve_rec(tri):
    l = len(tri)

    def find(i, j, sm):
        if i == l or len(tri[i]) == j: return sm
        current = tri[i][j] + sm
        return min(find(i + 1, j, current), find(i + 1, j + 1, current))

    return find(0, 0, 0)


def solve_dp(arr):
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
    return min(arr[len(arr) - 1])


tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(solve_rec(tri))
print(solve_dp(tri))
