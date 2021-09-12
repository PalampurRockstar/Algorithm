def find(arr, k):
    qb = dict()

    def solve(k, i=0):
        if k == 0: return 1
        if i == len(arr): return 0
        key = str(i) + ":" + str(k)
        if key in qb: return qb[key]
        qb[key] = solve(k, i + 1)
        if arr[i] <= k:
            qb[key] = qb[key] + solve(k - arr[i], i)
        return qb[key]
    return solve(k)


k = 15
coins = [3, 4, 6, 7, 9]
print(find(coins, k))
