import sys


def find(input, k):
    KD = input[0:1]
    for i, v in enumerate(input[1:]):
        KD.append(max(v, KD[i] + v))
    tm = -sys.maxsize
    cm = sum(input[0:k])
    tm = max(tm, cm)
    for right in range(k, len(input)):
        cm += input[right] - input[right - k]
        tm = max(tm, KD[right - k] + cm)
    return tm


k = 4
input = [2, 3, 1, -7, 6, -5, -4, 4, 3, 3, 2, - 9, -5, 6, 1, 2, 1, 4]
print(find(input, k))
