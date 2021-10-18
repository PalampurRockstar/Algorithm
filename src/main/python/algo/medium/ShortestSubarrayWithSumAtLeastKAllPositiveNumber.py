import sys


def find(input, k):
    length = len(input)
    if length == 0: return
    result = sys.maxsize
    left = 0
    cm = input[0]
    if cm >= k: tm = cm

    left = 0
    for right in range(1, length):
        if cm < k:cm += input[right]

        while k <= cm - input[left]:
            cm -= input[left]
            left += 1
        if cm >= k:result = min(right - left + 1, result)

    return result if result != sys.maxsize else 0


k = 51
input = [1, 4, 45, 6, 0, 19]
k = 280
input = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
k = 8
input = [1, 2, 4]

print(find(input, k))
