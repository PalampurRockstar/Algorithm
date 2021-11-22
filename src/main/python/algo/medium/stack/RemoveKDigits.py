def solve(num, k, S=[]):
    res = [str(i) for i in num]
    num = [int(i) for i in num]
    for i, v in enumerate(num):
        while S and num[S[-1]] >= v and k > 0:
            res[S.pop()] = 'x'
            k -= 1
        S.append(i)
    return "".join(res).replace('x', '')


num = "1432219"
k = 3
print(solve(num, k))
