def solve(A):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])

    minutes = [convert(e) for e in A]
    print(minutes)
    minutes.sort()
    M = float('inf')
    for x, y in zip(minutes, minutes[1:] + minutes[:1]):
        print(x, end="\t:\t")
        print(y)
        M = min(M, (y - x) % (24 * 60))
    return min((y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1]))


arr = ["23:59", "00:00"]
arr = ["00:00", "23:59", "00:00"]
print(solve(arr))
