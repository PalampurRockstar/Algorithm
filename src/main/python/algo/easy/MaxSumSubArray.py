def find(input):
    length = len(input)
    if length == 0: return 0
    tms = input[0]
    cms = input[0]
    for i in range(1, length):
        cms = max(input[i] + cms, input[i])
        tms = max(cms, tms)
    return tms


input = [2, 3, 4, 5, 6, 7, 8]
input = [4, 3, -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 1]
print(find(input))
