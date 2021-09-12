import sys


# leet code test
def find(arr, fee, sA=0):
    if len(arr) == 0: return 0
    bA = -arr[0]
    for i in arr[1:]:
        nBA = max(bA, sA - i)
        nSA = max(sA, bA + i - fee)
        bA = nBA
        sA = nSA
    return sA


# result=13
fee = 3
input = [0, 5, 7, 10, 6, 8, 12, 10, 12, 10, 13, 15]
# result=6
fee = 3
input = [1, 3, 7, 5, 10, 3]
# result=8
fee = 2
input = [1, 3, 2, 8, 4, 9]
# result=0
fee = 3
input = [9, 8, 7, 1, 2]
# result=0
fee = 0
input = [1]
# result=4
fee = 1
input = [2, 1, 4, 4, 2, 3, 2, 5, 1, 2]
print(find(input, fee))
