#It can be bit more optimized
def findByRecWrap(input, target, k):
    input.sort()
    return findByRec(input, target, [], k)


def findByRec(input, target, found, k):
    length = len(input)
    if length == 0: return []
    if k == 2:
        return findDoublet(input, target, found)
    result = []
    for i in range(length):
        including = findByRec(input[i + 1:], target - input[i], found + input[i:i + 1], k - 1)
        for i in including: result.append(i)
    return result


def findDoublet(input, target, found):
    length = len(input)
    right = length - 1
    left = 0
    result = []
    while left < right:
        if input[left] + input[right] == target:
            result.append((found + [input[left], input[right]]))
            left += 1
            right -= 1
        elif input[left] + input[right] < target:
            left += 1
        else:
            right -= 1

    return result


target = 7
input = [2, 5, 6, 7]
target = 9
input = [2, 4, 1, 5, 6, 3]
target = 2
input = [-2, 0, 1, 3]
target = 6
input = [4, 0, 6, 3, 5, 2, 1]

print(findByRecWrap(input, target, 3))
