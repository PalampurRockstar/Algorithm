# https://leetcode.com/problems/uncrossed-lines


def solve(arr1, arr2, dp={}):
    l1, l2 = len(arr1), len(arr2)

    def find(i1, i2):
        key = (i1, i2)
        if key in dp: return dp[key]
        if i1 == l1 or i2 == l2:
            return 0
        elif arr1[i1] == arr2[i2]:
            dp[key] = find(i1 + 1, i2 + 1) + 1
        else:
            dp[key] = max(find(i1 + 1, i2), find(i1, i2 + 1))
        return dp[key]

    return find(0, 0)


arr1 = [1, 4, 2]
arr2 = [1, 2, 4]

# arr1 = [2, 5, 1, 2, 5]
# arr2 = [10, 5, 2, 1, 5, 2]

arr1 = [2, 5, 1, 2, 5]
arr2 = [10, 5, 2, 1, 5, 2]
print(solve(arr1, arr2))
