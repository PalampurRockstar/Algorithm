def find(input, k):
    length = len(input)
    if length == 0: return []

    cm = input[0]
    tm = input[0]
    left = 0
    result = []
    for right in range(1, length):
        gap = right - left + 1
        if gap > k:
            cm -= input[left]
            left += 1

        if cm < 0:
            cm = input[right]
            left = right
        else:
            cm += input[right]
        if right - left + 1 == k:
            result.append(input[left:right + 1])
        tm = max(cm, tm)
    print(result)
    return tm


k = 3
input = [4, 1, 3, 2, 6]
print(find(input, k))
