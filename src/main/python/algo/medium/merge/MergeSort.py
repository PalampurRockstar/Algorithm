arr = [12, 11, 13, 5, 6, 7]


def merge(r_arr, l_arr):
    if len(r_arr) == 0: return l_arr
    if len(l_arr) == 0: return r_arr

    if l_arr[0] < r_arr[0]:
        return [l_arr[0]] + merge(r_arr, l_arr[1:])
    else:
        return [r_arr[0]] + merge(r_arr[1:], l_arr)


def sort(arr, s, e):
    if s == e: return [arr[s]]
    mid = (e + s) // 2
    return merge(sort(arr, s, mid), sort(arr, mid + 1, e))


print(sort(arr, 0, len(arr) - 1))
