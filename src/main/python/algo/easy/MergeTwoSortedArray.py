def solve(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)

    def merge(i, j, res=[]):
        if i == l1: return res + arr2[j:]
        if j == l2: return res + arr1[i:]
        if arr1[i] > arr2[j]:
            return merge(i, j + 1, res + [arr2[j]])
        else:
            return merge(i + 1, j, res + [arr1[i]])

    return merge(0, 0)


def solve(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)

    def merge(i, j, res=[]):
        if i == l1: return None
        if j == l2: return None
        if arr1[i] > arr2[j]:
            return merge(i, j + 1, res + [arr2[j]])
        else:
            return merge(i + 1, j, res + [arr1[i]])

    return merge(0, 0)


arr1 = [1, 7, 9]
arr2 = [2, 5, 6]
print(solve(arr1, arr2))
