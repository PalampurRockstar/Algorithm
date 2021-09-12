def findByLoop(arr):
    l = len(arr)
    arr.sort(key=lambda x: x[0])
    res = []
    for i in range(len(arr)):
        if i == l - 1:
            res.append(arr[i])
        elif arr[i + 1][0] >= arr[i][1]:
            res.append(arr[i])
        else:
            arr[i + 1][0] = min(arr[i][0], arr[i + 1][0])
            arr[i + 1][1] = max(arr[i][1], arr[i + 1][1])
    return res


input = [[8, 10], [1, 3], [7, 8], [9, 15], [2, 6]]
input = [[1, 3], [2, 6], [8, 10], [15, 18]]
input = [[1, 4], [0, 2], [3, 5]]

# [[1, 3],[2, 6],[7, 8],[8, 10],[9, 15]]
print(findByLoop(input))
