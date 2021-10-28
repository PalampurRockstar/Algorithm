# https://www.youtube.com/watch?v=NWMcj5QFW74
def solve(arr1, arr2):
    l1 = len(arr1)
    l2 = len(arr2)

    def place(i, n):
        t = i + 1
        while t < l2 and n > arr2[t]:
            arr2[t - 1] = arr2[t]
            t += 1
        arr2[t - 1] = n

    def find(i=0, j=0):
        if i == l1 or j == l2: return

        if arr1[i] < arr2[j]:
            find(i + 1, j)
        else:
            temp = arr1[i]
            arr1[i] = arr2[j]
            place(j, temp)
            find(i + 1, j)

    find()


arr1 = [1, 2, 7, 9]
arr2 = [3, 4, 6, 8]

solve(arr1, arr2)
print(arr1)
print(arr2)
