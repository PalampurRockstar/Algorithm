def find(arr, k):
    KD = arr[0:1]
    for i, v in enumerate(arr[1:]):
        KD.append(max(v, KD[i] + v))
    print(KD)
    cm = sum(arr[:k])
    tm = cm
    for right in range(k, len(arr)):
        cm += arr[right] - arr[right - k]
        tm = max(tm, KD[right - k] + cm)
    return tm


k = 4
input = [2, 3, 1, -7, 6, -5, -4, 4, 3, 3, 2, - 9, -5, 6, 1, 2, 1, 4]
k = 2
input = [-4, -2, 1, -3]
k = 2
input = [1, 1, 1, 1, 1, 1]
k = 4
input = [1, 2, 3, -10, -3]
print(find(input, k))
