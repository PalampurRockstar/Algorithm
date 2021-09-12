def find(n):
    res = ""
    while (n > 0):
        res += str(n & 1)
        n >>= 1
    return res


for i in range(10):
    print(find(i))
