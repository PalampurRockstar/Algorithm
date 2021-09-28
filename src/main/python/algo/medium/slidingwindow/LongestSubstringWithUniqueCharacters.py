import sys
from collections import defaultdict


def find(arr, char_index=defaultdict(lambda: 0), M=-sys.maxsize, b=0):
    for f, c in enumerate(arr):
        b = max(b, char_index[c] + 1)
        M = max(M, f - b + 1)
        char_index[c] = f
    return M


arr = "ABDEFGABEF"  # 6
arr = "GEEKSFORGEEKS"  # 7
arr = "BBBB"  # 1

print(find(arr))
