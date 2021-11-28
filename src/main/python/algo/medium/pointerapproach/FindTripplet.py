# https://leetcode.com/problems/3sum/

def solve(arr, k,res = set()):
    arr = sorted(arr)
    l = len(arr)
    for i in range(l - 2):
        left = i + 1
        right = l - 1
        while left < right:
            found = arr[i] + arr[left] + arr[right]
            if found == k:
                res.add((arr[i], arr[left], arr[right]))
                right -= 1
                left += 1
            elif found < k: left += 1
            else: right -= 1
    return list(res)


arr = [-1, 0, 1, 2, -1, -4]

print(solve(arr, 0))
