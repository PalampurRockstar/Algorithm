def find(input, k):
    accCount = {0: -1}
    acc = 0
    result = []
    for i, v in enumerate(input):
        acc += v
        accCount[acc] = i
        back = acc - k
        if back in accCount:
            result.append(input[accCount[back] + 1:i + 1])
    return result

# result=[[4, 1], [9, -2, 4, 1, -7], [1, -7, 2, 6, -5, 8], [8, -3], [6, -5, 8, -3, -7, 6], [-2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2]]
k = 5
input = [3, 9, - 2, 4, 1, -7, 2, 6, -5, 8, -3, -7, 6, 2, 1]
# result=[[3, 4], [7], [7, 2, -3, 1], [1, 4, 2]]
k=7
input = [3, 4, 7, 2, -3, 1, 4, 2]
print(find(input, k))
