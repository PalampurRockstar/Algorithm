def findUsingSet(input, target):
    result = []
    length = len(input)
    for i in range(length - 1):
        first = input[i]
        rest = target - first
        visited = set()
        for j in range(i + 1, length):
            third = input[j]
            second = rest - third
            if second in visited:
                result.append((second, third, first))
            else:
                visited.add(third)
    return result


def findUsingPointer(input, target):
    input.sort()
    result = []
    length = len(input)
    for i in range(length - 2):
        rP = length - 1
        lP = i + 1
        rAmt = target - input[i]
        while rP > lP:
            sumOfTwo = (input[rP] + input[lP])
            if rAmt == sumOfTwo:
                # found
                result.append((input[i], input[lP], input[rP]))
                rP -= 1
                lP += 1
            elif rAmt < sumOfTwo:
                rP -= 1
            else:
                lP += 1
    return result


def findByRec(input, target, found):
    if len(found) == 3 and target == 0: return print(found)
    if len(input) == 0 : return

    findByRec(input[1:], target - input[0], found + input[0:1])
    findByRec(input[1:], target, found)


target = 24
input = [12, 3, 4, 1, 6, 9]

target = 2
input = [-2, 0, 1, 3]

target = -2
input = [0, -1, 2, -3, 1]

print(findUsingSet(input, target))
print(findUsingPointer(input, target))
findByRec(input, target, [])
