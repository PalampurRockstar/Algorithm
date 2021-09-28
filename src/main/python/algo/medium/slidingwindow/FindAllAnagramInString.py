# https://leetcode.com/problems/find-all-anagrams-in-a-string/

def find(str, p):
    find_map = dict()
    find_count = 0
    for c in p:
        find_map[c] = find_map[c] + 1 if c in find_map else 1
        find_count += 1
    found_map = dict()
    found_count = 0
    res = []
    b = 0
    for f, c in enumerate(str):
        if c in find_map:
            found_map[c] = found_map[c] + 1 if c in found_map else 1
            found_count += 1
        else:
            found_count = 0
            found_map = dict()
            b = f + 1

        if c in found_map and c in find_map and found_map[c] > find_map[c]:
            while str[b] != c:
                if str[b] in found_map:
                    found_map[str[b]] -= 1
                    found_count -= 1
                b += 1
            found_map[str[b]] -= 1
            found_count -= 1
            b += 1

        if found_count == find_count:
            res.append(b)
            found_map[str[b]] -= 1
            found_count -= 1
            b += 1
    return res


s = "abcdecdbacb"
p = "abc"

s = "cbaebabacd"
p = "abc"

s = "abaacbabc"
p = "abc"

print(find(s, p))
