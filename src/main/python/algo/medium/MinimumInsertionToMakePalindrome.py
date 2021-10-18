def findByRecMemorization(input, indexes, qb):
    left, right = indexes
    key = str(left) + ":" + str(right)
    if key in qb: return qb[key]
    if right < 0 or left > len(input) - 1 or left > right:
        qb[key] = []
        return qb[key]
    if (right - left + 1) == 0 or (right - left + 1) == 1:
        qb[key] = [input[left:right + 1]]
        return qb[key]
    if input[left] == input[right]:
        qb[key] = [input[left]] + findByRecMemorization(input, (left + 1, right - 1), qb) + [input[left]]
        return qb[key]
    else:
        leftList = findByRecMemorization(input, (left, right - 1), qb) + ['_']
        rightList = ['_'] + findByRecMemorization(input, (left + 1, right), qb)
        qb[key] = leftList if len(leftList) > len(rightList) else rightList
        return qb[key]


def find_by_tabulation(input):
    length = len(input)
    dp = [[0 for j in range(length)] for i in range(length)]
    for g in range(length):
        for j in range(g, length):
            i = j - g
            if g == 0:
                dp[i][j] = 0
            elif g == 1:
                dp[i][j] = 0 if input[i] == input[j] else 1
            else:
                if input[i] == input[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1
    return dp[0][length - 1]


input = "aabaaba"
input = "leetcode"

print(findByRecMemorization(input, (0, len(input) - 1), dict()).count("_"))
print(find_by_tabulation(input))
