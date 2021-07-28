def find(input, b, f):
    length = len(input)
    if length == 0 or not (0 < b < length) or not (- 1 < f < length) or b > f: return 0
    accList = input[0:1]
    for i in input[1:]:
        accList.append(accList[len(accList) - 1] + i)
    print(accList)
    return accList[f] - accList[b - 1]


input = [2, -3, 4, 1, -2, 4, 7, -1, 7, 9]
print(find(input, 7, 8))
