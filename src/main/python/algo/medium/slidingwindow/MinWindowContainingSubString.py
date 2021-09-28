from collections import defaultdict
import sys


def find(arr, p, find_map=defaultdict(lambda: 0), found_map=defaultdict(lambda: 0), find_count=0, found_count=0, b=0,
         M=sys.maxsize):
    for c in p:
        find_map[c] += 1
        find_count += 1
    for f, c in enumerate(arr):
        found_map[c] += 1
        if find_map[c] > 0: found_count += 1
        if found_count >= find_count:
            while found_map[arr[b]] > find_map[arr[b]]:
                found_map[arr[b]] -= 1
                if find_map[arr[b]] > 0: found_count -= 1
                b += 1
            M = min(M, f - b + 1)
    return M


arr = "ADOBECODEBANC"
p = "ABC"
print(find(arr, p))
