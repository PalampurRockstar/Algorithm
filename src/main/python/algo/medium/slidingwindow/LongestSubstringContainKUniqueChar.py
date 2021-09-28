# https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
import sys


def find(arr, k, b=0, M=-sys.maxsize, visited=set(), char_map=dict()):
    for f, c in enumerate(arr):
        char_map[c] = char_map[c] + 1 if c in char_map else 1
        visited.add(c)
        if len(visited) == k: M = max(M, f - b + 1)
        while len(visited) > k:
            char_map[arr[b]] -= 1
            if char_map[arr[b]] == 0: visited.remove(arr[b])
            b += 1
    return M if M != -sys.maxsize else 0


arr = "aabbcc"
k = 1
# result 2

arr = "aabbcc"
k = 3
# result 6


arr = "aaabbb"
k = 3
print(find(arr, k))
