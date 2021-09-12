def find(arr, dict, qb, index=0):
    l = len(arr)
    if index == l: return True
    if index in qb: return qb[index]
    for i in range(index, l):
        if arr[index:i + 1] in dict and find(arr, dict, qb, i + 1):
            qb[index] = True
            return True
    qb[index] = False
    return False


str = "applepenapple"
words = set({"apple", "pen"})

print(find(str, words, dict()))
