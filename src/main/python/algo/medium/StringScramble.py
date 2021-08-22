def find_rec(s1, s2):
    if len(s1) != len(s2): return False
    if s1 == s2: return True
    l = len(s1)
    for k in range(1, len(s2)):
        if (find_rec(s1[:k], s2[:k]) and find_rec(s1[k:], s2[k:])) or \
                find_rec(s1[:k], s2[l - k:]) and find_rec(s1[k:], s2[:l - k]):
            return True
    return False


def find_mem(s1, s2, qb):
    if len(s1) != len(s2): return False
    if s1 == s2: return True
    l = len(s1)
    key = s1 + ":" + s2
    if key in qb: return qb[key]
    for k in range(1, len(s2)):
        if (find_mem(s1[:k], s2[:k], qb) and find_mem(s1[k:], s2[k:], qb)) or \
                find_mem(s1[:k], s2[l - k:], qb) and find_mem(s1[k:], s2[:l - k], qb):
            qb[key] = True
            return True
    qb[key] = False
    return False


s1 = "abcde"
s2 = "caebd"

print(find_rec(s1, s2))
print(find_mem(s1, s2, dict()))
