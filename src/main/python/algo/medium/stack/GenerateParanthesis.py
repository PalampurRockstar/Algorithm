# https://leetcode.com/problems/generate-parentheses/submissions/
def solve(n):
    res = []

    def find(found, left, right):
        if left == 0 and right == 0: return res.append(found)
        if left > 0:
            find(found + "(", left - 1, right)
        if left < right:
            find(found + ")", left, right - 1)

    find("", n, n)
    return res


n = 3
print(solve(n))
