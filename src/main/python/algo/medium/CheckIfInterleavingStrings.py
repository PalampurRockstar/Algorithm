def find(s1, s2, s3, qb=dict()):
    if len(s1) == 0 and len(s2) == 0 and len(s3) == 0: return True
    if len(s3) == 0: return False
    key = s1 + ":" + s2 + ":" + s3
    if key in qb: return qb[key]
    if len(s1) > 0:
        if s3[0] == s1[0] and find(s1[1:], s2, s3[1:], qb):
            qb[key] = True
            return True
    if len(s2) > 0:
        if s3[0] == s2[0] and find(s1, s2[1:], s3[1:], qb):
            qb[key] = True
            return True
    qb[key] = False
    return False


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

print(find(s1, s2, s3))
