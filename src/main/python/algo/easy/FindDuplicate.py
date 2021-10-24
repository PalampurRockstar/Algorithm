def solve(nums, visited=set(), res=[]):
    for v in nums:
        if v in visited:
            res.append(v)
        visited.add(v)
    return res


arr = [4, 3, 2, 7, 8, 2, 3, 1]
arr = [1,1,2]
print(solve(arr))
