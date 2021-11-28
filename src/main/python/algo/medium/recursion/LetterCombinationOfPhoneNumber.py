# https://leetcode.com/problems/letter-combinations-of-a-phone-number

def solve(arr):
    mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []

    def recurse(found, digits):
        nonlocal res
        if len(found) == len(arr):
            return res.append(found)

        for i, d in enumerate(digits):
            for char in mapping[d]:
                recurse(found + char, digits[i + 1:])

    recurse("", arr)
    return res


arr = "23"
print(solve(arr))
