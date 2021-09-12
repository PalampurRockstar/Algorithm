# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# def find(arr, n, left, right, flag=False):
#     if left > right: return None
#     mid = int((left + right) / 2)
#     if not flag:
#         if arr[right] > arr[left]:
#             return find(arr, n, left, right, True)
#         else:
#             if arr[left] < arr[mid]:
#                 return find(arr, n, mid + 1, right, flag)
#             elif arr[right] > arr[mid]:
#                 return find(arr, n, left, mid - 1, flag)
#             else:
#                 if arr[right] > n:
#                     return find(arr, n, left, right, True)
#     if arr[mid] < n:
#         return find(arr, n, mid + 1, right, True)
#     elif arr[mid] > n:
#         return find(arr, n, left, mid - 1, True)
#     else:
#         return mid
#
#
# arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# n = 3
# print(find(arr, n, 0, len(arr) - 1))
