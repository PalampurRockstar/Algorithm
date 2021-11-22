def solve(arr1, arr2):
    if len(arr1) > len(arr2): arr2, arr1 = arr1, arr2
    s = 0
    e = len(arr1)
    tl = len(arr1) + len(arr2)
    while s <= e:
        i = (s + e) // 2
        j = (tl + 1) // 2 - i
        f_left = float('-inf') if i == 0 else arr1[i - 1]
        f_right = float('inf') if i == len(arr1) else arr1[i]

        s_left = float('-inf') if j == 0 else arr2[j - 1]
        s_right = float('inf') if j == len(arr2) else arr2[j]

        if f_left <= s_right and s_left <= f_right:
            if tl % 2 == 0:
                return (max(f_left, s_left) + min(s_right, f_right)) / 2
            else:
                return max(f_left, s_left)
        elif f_left > s_right:
            e = i - 1
        else:
            s = i + 1


arr1 = [1, 2]
arr2 = [3, 4]
print(solve(arr1, arr2))
