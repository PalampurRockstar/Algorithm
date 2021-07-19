import sys


def findMaxProfitTracsaction(input):
    hp = 0
    minBuy = sys.maxsize
    for i in input:
        minBuy = min(minBuy, i)
        hp = max(i - minBuy, hp)
    return hp


input = [7, 1, 5, 3, 6, 4]
print(findMaxProfitTracsaction(input))
