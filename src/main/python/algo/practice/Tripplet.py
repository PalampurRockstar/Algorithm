def find_triplet_using_set(arr, k):
    l = len(arr)
    for i in range(l - 2):
        first = arr[i]
        to_find = k - first
        found = find_doublet(arr[i + 1:], to_find)
        if found:
            return first, found[0], found[1]
    return None


def find_doublet(arr, k):
    visited = set()
    for second in arr:
        if k - second in visited:
            return k - second, second
        else:
            visited.add(second)
    return None


def find_triplet_using_pointer(arr, k):
    l = len(arr)
    sorted(arr)
    for i in range(l - 2):
        first = arr[i]
        to_find = k - first
        found = find_doublet(arr[i + 1:], to_find)
        if found:
            return first, found[0], found[1]
    return None


def find_doublet(arr, k):
    left = 0
    right = len(arr) - 1
    while left < right:
        if k < arr[right] + arr[left]:
            right -= 1
        elif k > arr[right] + arr[left]:
            left += 1
        else:
            return arr[right], arr[left]
    return None


target = 24
input = [12, 3, 4, 1, 6, 9]
print(find_triplet_using_set(input, target))
print(find_triplet_using_pointer(input, target))
