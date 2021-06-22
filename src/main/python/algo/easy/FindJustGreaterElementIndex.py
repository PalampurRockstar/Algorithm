def ceilIndex(T, n):
    length = len(T)
    index = -1
    lb = 0
    rb = length
    while lb <= rb and lb < length and rb > -1:
        mid = int((lb + rb) / 2)
        if T[mid] == n or lb == rb:
            return mid
        elif T[mid] > n:
            if (mid - 1) > -1 and T[mid - 1] < n:
                return mid
            else:
                rb = mid - 1
        else:
            if (mid + 1) < len(T) and T[mid + 1] > n:
                return mid + 1
            else:
                lb = mid + 1
    if rb < 0:
        return 0
    else:
        return -1


T = [1, 2, 9, 30, 44, 50, 55, 60, 72, 82]
print(ceilIndex(T, -1) == 0)
print(ceilIndex(T, 10) == 3)
print(ceilIndex(T, 3) == 2)
print(ceilIndex(T, 89) == -1)
