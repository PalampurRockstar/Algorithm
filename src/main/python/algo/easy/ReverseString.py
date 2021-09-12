def reverse_inplace(s):
    j = len(s) - 1
    i = 0
    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


A = ['s', 'o', 'u', 'r', 'a', 'b', 'h']
print(reverse_inplace(A))
