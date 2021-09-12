# https://www.geeksforgeeks.org/chocolate-distribution-problem/

def find(arr, n):
    if len(arr) < n: return 0
    arr.sort()
    min_dif = arr[n - 1] - arr[0]
    for i in range(n, len(arr)):
        min_dif = min(min_dif, arr[i] - arr[i - n + 1])  # carefull about i-n+1
    return min_dif


arr = [3, 4, 1, 9, 56, 7, 9, 12]
print(find(arr, 5))
