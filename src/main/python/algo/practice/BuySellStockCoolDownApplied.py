import sys


def find(arr, sa=0, ca=0):
    if len(arr) == 0: return 0
    ba = -arr[0]
    for v in arr[1:]:
        cba = max(ba, ca - v)
        csa = max(sa, ba + v)
        ca = max(ca, sa)
        sa = csa
        ba = cba
    return sa


fee = 3
arr = [2, 1, 4, 4, 2, 3, 2, 5, 1, 2]
print(find(arr, fee))
