# https://www.geeksforgeeks.org/maximum-sum-iarri-among-rotations-given-array/
# Input: arr[] = {8, 3, 1, 2}
# Output: 29
# Explanation: Lets look at all the rotations,
# {8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
# {3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
# {1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
# {2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*3 = 17


def find(arr):
    l = len(arr)
    SUM = sum(arr)
    s0 = sum([i * v for i, v in enumerate(arr)])
    MAX = s0
    for i in range(len(arr)):
        s1 = s0 + SUM - l * arr[l - 1 - i];
        MAX = max(MAX, s1)
        s0 = s1
    return MAX


arr = [8, 3, 1, 2]
print(find(arr))
