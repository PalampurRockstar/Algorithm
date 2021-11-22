# https://leetcode.com/problems/wildcard-matching/

def solve(arr, pat):
    sl, pl = len(arr), len(pat)

    def find(s, p):
        print(s, p)
        if p == pl: return s == sl
        if pat[p] == '*':
            return find(s, p + 1) or find(s + 1, p + 1) or find(s + 1, p)
        elif s < sl and pat[p] == arr[s] or pat[p] == '?':
            return find(s + 1, p + 1)
        else:
            return False

    return find(0, 0)


def solve_by_index(arr: str, pat: str):
    def find(s, p):
        if p == len(pat): return s == len(arr)
        if s == len(arr): return set(pat[p:]) == {'*'}
        if pat[p] == '*':
            return find(s, p + 1) or find(s + 1, p + 1) or find(s + 1, p)
        elif arr[s] == pat[p] or pat[p] == '?':
            return find(s + 1, p + 1)
        else:
            return False

    return find(0, 0)


# print(solve("adceb", "*a*b"))
# print(solve("aa", "a"))
# print(solve("aa", "*"))
# print(solve("ca", "ab"))
# print(solve("adceb", "*a*b"))
# print(solve("acdcb", "a*c?b"))
# print(solve("", "******"))
# print(solve("a", "aa"))
# print(solve("abcabczzzde", "*abc???de*"))
# print(isMatch("abcabczzzde", "*abc???de*"))
# print(solve("acdcb", "a*c?b"))
# solve_by("acdcb", "a*c?b")
# solve_by_index("acdcb", "a*c?b")

solve_by_index("aa", "a")
