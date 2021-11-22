def solve(arr):
    visited = set()
    expected_sum = 0
    actual_sum = 0
    repeated = None
    for index, each in enumerate(arr):
        if each in visited: repeated = each
        actual_sum += each
        expected_sum += (index + 1)
        visited.add(each)
    return expected_sum - (actual_sum - repeated), repeated


arr = [4, 3, 6, 2, 1, 1]
print(solve(arr))
