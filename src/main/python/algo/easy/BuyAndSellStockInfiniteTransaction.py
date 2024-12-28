# Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

def find(input):
    if len(input) == 0: return None
    lis = input[0]
    result = []
    for i in range(len(input)):
        if i == len(input) - 1:
            if lis < input[i]:
                result.append((lis, input[i]))
        elif input[i] > input[i + 1]:
            result.append((lis, input[i]))
            lis = input[i + 1]
    return sum([i[1] - i[0] for i in result])


input = [4, 4, 6, 5, 6, 3, 4, 6, 7, 7, 6, 8, 3, 4, 1, 6, 7, 5]
# input = [7, 1, 5, 3, 6, 4]


print(find(input))


def solve(input):
    l = len(input)
    minSoFar = input[0]
    total = 0
    for index in range(l):
        if index + 1 < l and input[index] > input[index + 1]:
            total += input[index] - minSoFar
            minSoFar = input[index + 1]
        elif index + 1 == l and minSoFar < input[index]:
            total += input[index] - minSoFar
    return total


print(solve(input))
