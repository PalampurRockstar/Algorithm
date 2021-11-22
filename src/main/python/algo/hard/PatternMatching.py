# https://leetcode.com/problems/regular-expression-matching
def solve(s, p):
    lenS, lenP = len(s), len(p)

    def find(i, j):
        if j >= lenP: return i == lenS
        if (j + 1) < lenP and p[j + 1] == "*":
            return find(i, j + 2) or (i < lenS and (s[i] == p[j] or p[j] == '.') and find(i + 1, j))
        elif i < lenS and (s[i] == p[j] or p[j] == '.'):
            return find(i + 1, j + 1)
        else:
            return False

    return find(0, 0)


def solve_by_rec(s, p):
    lenS, lenP = len(s), len(p)
    cache = {}

    def find(i, j):
        nonlocal cache
        if j >= lenP: return i == lenS
        key = (i, j)
        if key in cache: return cache[key]
        if (j + 1) < lenP and p[j + 1] == "*":
            cache[key] = find(i, j + 2) or (i < lenS and (s[i] == p[j] or p[j] == '.') and find(i + 1, j))
        elif i < lenS and (s[i] == p[j] or p[j] == '.'):
            cache[key] = find(i + 1, j + 1)
        else:
            cache[key] = False
        return cache[key]

    return find(0, 0)


print(solve("aab", "c*a*b"))
print(solve("aa", "a"))
print(solve("mississippi", "mis*is*p*."))
print(solve("aa", "a*"))
