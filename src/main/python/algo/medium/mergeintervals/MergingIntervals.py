def findByLoop(input):
    input.sort(key=lambda x: x[0])

    result = []
    for i in range(len(input)):
        next = input[i + 1] if i + 1 < len(input) else []
        current = input[i]
        if next != [] and current[1] > next[0]:
            if current[1] < next[1]:
                input[i + 1] = [current[0], next[1]]
            else:
                input[i + 1] = current
        else:
            result.append(input[i])
    return result


def findByLoopWithExtraVariable(input):
    input.sort(key=lambda x: x[0])
    result = []
    continues = []
    for i in range(len(input)):
        next = input[i + 1] if i + 1 < len(input) else []
        current = continues if continues != [] else input[i]
        if next != [] and current[1] > next[0]:
            if current[1] < next[1]:
                continues = [current[0], next[1]]
        else:
            result.append(continues if continues != [] else input[i])
    return result


input = [[8, 10], [1, 3], [7, 8], [9, 15], [2, 6]]
input = [[1, 3], [2, 6], [8, 10], [15, 18]]
input = [[1, 4], [0, 2], [3, 5]]
print(findByLoop(input))
print(findByLoopWithExtraVariable(input))
