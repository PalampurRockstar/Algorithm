import sys


def find(str, pat, to_find=dict(), found=dict(), found_count=0, res=sys.maxsize, b=0):
    for ch in pat: to_find[ch] = to_find[ch] + 1 if ch in to_find else 0
    for f, fv in enumerate(str):
        if fv in to_find:
            found[fv] = found[fv] + 1 if fv in found else 1
            found_count += 1
        while found_count > len(pat) and ((str[b] not in to_find) or found[str[b]] > to_find[str[b]]):
            if str[b] in to_find:
                found_count -= 1
                found[str[b]] -= 1
            b += 1
        if found_count >= len(pat):
            res = min(res, f - b + 1)
    return res


str = "this ttis a test string"
pat = "tist"

print(find(str, pat))
