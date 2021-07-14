def findByRec(start, end):
    if len(end) == 1:
        print(start + end)
    for i in range(len(end)):
        findByRec(start + end[i], end[0:i] + end[i + 1:])

findByRec("", "22")
