def solve_rec(tri):
    l = len(tri)

    def find(i, j, sm):
        if i == l or len(tri[i]) == j: return sm
        current = tri[i][j] + sm
        return min(find(i + 1, j, current), find(i + 1, j + 1, current))

    return find(0, 0, 0)


def solve_dp(tri):
    l = len(tri)
    for i in range(1, tri):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] += tri[i - 1][j]
            elif j == len(tri) - 1:
                tri[i][j] += tri[i - 1][j - 1]
            else:
                tri[i][j] = min(tri[i - 1][j - 1], tri[i - 1][j])

    return min(tri[l - 1])


tri = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(solve_rec(tri))
