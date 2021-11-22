import sys


def solve(arr, fee):
    ba = -arr[0]
    sa = 0
    for each in arr[1:]:
        nba = max(sa - each, ba)
        nsa = max(ba + each - fee, sa)
        ba = nba
        sa = nsa
    return sa


fee = 3
arr = [0, 5, 7, 10, 6, 8, 12, 10, 12, 10, 13, 15]

arr = [1, 3, 2, 8, 4, 9]
fee = 2
print(solve(arr, fee))
