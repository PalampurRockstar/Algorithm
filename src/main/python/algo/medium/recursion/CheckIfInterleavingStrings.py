def find(s1, s2, s3):
    qb = dict()

    def solve(i1, i2, i3):
        if len(s1) == i1 and i2 == len(s2) and i3 == len(s3): return True
        if i3 == len(s3): return False
        key = str(i1) + ":" + str(i2) + ":" + str(i3)
        if key in qb: return qb[key]
        if i2 != len(s2) and s3[i3] == s2[i2] and solve(i1, i2 + 1, i3 + 1):
            qb[key] = True
            return True
        if i1 != len(s1) and s3[i3] == s1[i1] and solve(i1 + 1, i2, i3 + 1):
            qb[key] = True
            return True
        qb[key] = False
        return False

    return solve(0, 0, 0)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print(find(s1, s2, s3))
