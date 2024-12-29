# https://leetcode.com/problems/4sum

arr_to_str = lambda inputArr: ', '.join(map(str, sorted(inputArr)))


def solve(arr, target):
    size = len(arr)
    arr.sort()
    right = size - 1
    result = set()
    for i in range(size - 3):
        for j in range(i + 1, size - 2):
            left = j + 1
            while left < right:
                possibleSum = arr[i] + arr[j] + arr[left] + arr[right]
                if possibleSum == target:
                    result.add(arr_to_str([arr[i], arr[j], arr[left], arr[right]]))
                    print(result)
                    break
                elif possibleSum < target:
                    left += 1
                else:
                    right -= 1

    return [[int(key) for key in eachKey.split(',')] for eachKey in result]


# print(solve([1, 0, -1, 0, -2, 2], 0))

print(solve([-3, -1, 0, 2, 4, 5], 0))
