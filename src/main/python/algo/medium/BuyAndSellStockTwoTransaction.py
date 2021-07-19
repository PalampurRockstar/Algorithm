import sys

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

#Leet code tested
def findMaxProfitTracsactionMultipleLoop(input):
    lsf = sys.maxsize
    hp = 0
    ltr = [0] * len(input);

    for i, v in enumerate(input):
        lsf = min(lsf, v)
        hp = max(v - lsf, hp)
        if i > 0: ltr[i] = max(hp, ltr[i - 1])
    hp = 0
    msf = 0
    rtl = [0] * len(input)
    for i, v in reversed(list(enumerate(input))):
        msf = max(msf, v)
        hp = max(msf - v, hp)
        if i < len(input) - 1: rtl[i] = max(hp, rtl[i + 1])
    tm = 0
    for l, r in zip(ltr, rtl):
        tm = max(tm, l + r)
        print(l, end=" : ")
        print(r, end=" : ")
        print(str(l + r))
    return tm


input = [7, 1, 5, 3, 6, 4]
input = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 20, 40, 45, 71, 50, 55]
input = [3, 3, 5, 0, 0, 3, 1, 4]
input = [1, 2, 3, 4, 5]
input = [7, 6, 4, 3, 1]
input = [1, 2]
print(findMaxProfitTracsactionMultipleLoop(input))
