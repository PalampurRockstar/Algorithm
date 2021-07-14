def findUsingSet(input, target):
    s = set()
    result = []
    for i in input:
        if target - i in s:
            result.append((i, target - i))
        else:
            s.add(target - i)
    return result


def findUsingPointer(input, target):
    length = len(input)
    input.sort()
    left = 0
    right = length - 1
    result = []
    while right > left:
        if input[left] == input[left + 1]:
            left += 1
            continue
        if input[left] + input[right] == target:
            result.append((input[left], input[right]))
            right -= 1
            left += 1
        elif input[left] + input[right] < target:
            left += 1
        else:
            right -= 1
    return result


input = [2, 2, 3, 4, 2, 8, 8]
target = 10
print(findUsingSet(input, target))
print(findUsingPointer(input, target))
