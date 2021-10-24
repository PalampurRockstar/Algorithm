def solve(n):
    def climb(n):
        if n < 0: return 0
        if n == 0:
            return 1
        else:
            return climb(n - 1) + climb(n - 2)

    return climb(n)


print(solve(5))
