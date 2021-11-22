def find(s, words, i, qb):
    l = len(s)
    if i >= l: return True
    if i in qb: return qb[i]
    for j in range(i + 1, l + 1):
        if s[i:j] in words and find(s, words, j, qb):
            qb[i] = True
            return qb[i]
    qb[i] = False
    return qb[i]


def findStr(s, words):
    if len(s) == 0: return True
    for j in range(1, len(s) + 1):
        if s[0:j] in words and findStr(s[j:], words): return True
    return False


def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i]:
            for j in range(i, len(s)):
                print(s[i: j + 1])
                if s[i: j + 1] in wordDict:
                    dp[j + 1] = True
    return dp[-1]


str = "applepenapple"
words = set({"apple", "pen"})
print(find(str, words, 0, dict()))
print(findStr(str, words))
print(wordBreak(str, words))
