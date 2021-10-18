w1 = "horse"
w2 = "ros"


def solve_1(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    qb = dict()

    def find(i1, i2):
        if i1 == l1 and i2 == l2: return 0
        if i1 == l1: return ((l2 - 1) - i2) + 1
        if i2 == l2: return ((l1 - 1) - i1) + 1
        key = str(i1) + ":" + str(i2)
        if key in qb: return qb[key]
        if s1[i1] == s2[i2]:
            qb[key] = find(i1 + 1, i2 + 1)
        else:
            qb[key] = min(find(i1 + 1, i2 + 1),
                          min(find(i1, i2 + 1),
                              find(i1 + 1, i2))) + 1
        return qb[key]

    return find(0, 0)


def solve_2(s1, s2, qb=dict()):
    if len(s1) == 0: return len(s2)
    if len(s2) == 0: return len(s1)
    key = s1 + ":" + s2
    if key in qb: return qb[key]
    if s1[0] == s2[0]:
        qb[key] = solve_2(s1[1:], s2[1:], qb)
    else:
        qb[key] = min(solve_2(s1[1:], s2, qb), min(solve_2(s1, s2[1:], qb), solve_2(s1[1:], s2[1:], qb))) + 1
    return qb[key]


print(solve_1(w1, w2))
print(solve_2(w1, w2))
