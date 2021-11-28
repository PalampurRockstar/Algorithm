def solve(str1, str2):
    def find(i, j):
        if i == len(str1): return len(str2[j:])
        if j == len(str2): return len(str1[i:])
        if str1[i] == str2[j]:
            return find(i + 1, j + 1)
        else:
            return min(find(i + 1, j), find(i, j + 1)) + 1

    return find(0, 0)


str1 = "heat"
str2 = "hit"
print(solve(str1, str2))
