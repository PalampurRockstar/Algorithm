def evenSumK(arr, N, K):
    if K > N: return -1
    maxSum = 0
    Even = []
    Odd = []
    for i in range(N):
        if arr[i] % 2:
            Odd.append(arr[i])
        else:
            Even.append(arr[i])
    Odd.sort()
    Even.sort()
    i = len(Even) - 1
    j = len(Odd) - 1
    while K > 0:
        if K % 2 == 1:
            if i >= 0:
                maxSum += Even[i]
                i -= 1
            else:
                return -1
            K -= 1
        elif i >= 1 and j >= 1:
            if Even[i] + Even[i - 1] <= Odd[j] + Odd[j - 1]:
                maxSum += Odd[j] + Odd[j - 1]
                j -= 2
            else:
                maxSum += Even[i] + Even[i - 1]
                i -= 2
            K -= 2
        elif i >= 1:
            maxSum += Even[i] + Even[i - 1]
            i -= 2
            K -= 2
        elif j >= 1:
            maxSum += Odd[j] + Odd[j - 1]
            j -= 2
            K -= 2

    return maxSum
