def solve(nums):
    prefix = [1]
    prod = 1
    for n in nums:
        prod *= n
        prefix.append(prod)

    suffix = [1]
    prod = 1
    for n in reversed(nums):
        prod *= n
        suffix.append(prod)
    suffix.reverse()

    output = [prefix[i] * suffix[i + 1] for i in range(len(nums))]

    return output
