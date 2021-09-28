from collections import defaultdict


# Function to find largest
# subarray with no duplicates
def largest_subarray(a, n):
    index = defaultdict(lambda: 0)
    M = 0
    b = 0
    for f, v in enumerate(a):
        b = max(index[v], b)
        M = max(M, f - b + 1)
        index[v] = f + 1

    # Return final ans
    return M


# Driver Code
arr = [1, 2, 3, 4, 5, 1, 2, 3]
n = len(arr)

# Function call
print(largest_subarray(arr, n))
