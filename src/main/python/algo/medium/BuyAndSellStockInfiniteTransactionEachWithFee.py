import sys


# my solution didn't work for all test cases
# def find(input, fee):
#     if len(input) == 1: return 0
#     tm = 0
#     cm = -sys.maxsize
#     left = 0
#     right = 1
#     while left <= right < len(input):
#         diff = input[right] - input[left]
#         cm = max(cm, diff)
#         if cm - fee >= 0:
#             if right == len(input) - 1:
#                 tm = cm - fee + tm
#             elif (cm - diff) > fee:
#                 tm = cm - fee + tm
#                 cm = 0
#                 left = right
#         else:
#             left = right
#         right += 1
#     return tm

# leet code test
def find(input, fee):
    bA = -input[0]
    sA = 0
    for i in input[1:]:
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
