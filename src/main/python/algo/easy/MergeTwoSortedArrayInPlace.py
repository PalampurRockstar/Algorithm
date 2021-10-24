def merge(nums1, n, nums2, m) -> None:
    while m > 0 and n > 0:
        if nums1[n - 1] > nums2[m - 1]:
            nums1[n + m - 1] = nums1[n - 1]
            n -= 1
        else:
            nums1[n + m - 1] = nums2[m - 1]
            m -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
n = 3
nums2 = [2, 5, 6]
m = 3
print(merge(nums1, n, nums2, m))
