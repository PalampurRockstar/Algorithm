# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict


def solve(arr, res=[]):
    map = defaultdict(lambda: [])
    for e in arr: map[str(sorted(e))].append(e)
    return map.values()


arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
arr = ["ddddddddddg", "dgggggggggg"]
print(solve(arr))
