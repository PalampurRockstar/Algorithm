import sys


def find(arr, fee, sa=0):
    if len(arr) == 0: return 0
    ba = -arr[0]
    for v in arr[1:]:
        csa = max(sa, ba + v - fee)
        cba = max(ba, sa - v)
        sa = csa
        ba = cba
    return sa


fee = 3
arr = [0, 5, 7, 10, 6, 8, 12, 10, 12, 10, 13, 15]
print(find(arr, fee))
