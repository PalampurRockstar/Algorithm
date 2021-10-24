def solve(s1, s2, qb=dict()):
    def find(i, j):
        nonlocal qb
        if len(s1) == i or len(s2) == j: return 0
        key = i, j
        if key in qb: return qb[key]
        if s1[i] == s2[j]:
            qb[key] = find(i + 1, j + 1) + 1
        else:
            qb[key] = max(find(i, j + 1), find(i + 1, j))
        return qb[key]

    return find(0, 0)


s1 = "abcde"
s2 = "ace"

print(solve(s1, s2))
