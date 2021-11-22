# https://leetcode.com/problems/iterator-for-combination

class CombinationIterator:

    def __init__(self, characters: str, n: int):
        self.res = self.solve(characters, n)

        self.state = 0

    def next(self) -> str:
        result = self.res[self.state]
        self.state += 1
        return result

    def solve(self, arr, k):
        res = []

        def find(found, index, count):
            nonlocal res
            if count == 0: return res.append(found)
            if len(arr) == index: return
            for i in range(index, len(arr)):
                find(found + arr[i], i + 1, count - 1)

        find("", 0, k)
        return res

    def hasNext(self) -> bool:
        return self.state < len(self.res)


# iterator = CombinationIterator("sourabh", 2)
# print(iterator.next())
# print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())
# print(iterator.next())
# print(iterator.hasNext())


def solve(arr, k):
    res = []

    def find(found, index, count):
        nonlocal res
        if count == 0: return res.append(found)
        if len(arr) == index: return
        for i in range(index, len(arr)):
            find(found + arr[i], i + 1, count - 1)

    find("", 0, k)
    return res


arr = "abcd"
k = 3
print(solve(arr, k))
