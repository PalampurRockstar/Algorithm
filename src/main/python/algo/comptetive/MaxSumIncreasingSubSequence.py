def max_sum(l1, l2):
    return l1 if sum(l1) > sum(l2) else l2


def find(arr, found=[]):
    if len(arr) == 0: return found
    if len(found) == 0: return find(arr[1:], [arr[0]])

    exclude = find(arr[1:], found)
    if found[-1] <= arr[0]:
        return max_sum(find(arr[1:], found + [arr[0]]), exclude)
    else:
        return max_sum(find(arr[1:], [arr[0]]), exclude)


arr = [1, 101, 2, 3, 100, 4, 5]
print(find(arr))
