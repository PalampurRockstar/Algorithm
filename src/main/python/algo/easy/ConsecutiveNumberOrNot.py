
import sys

def find(arr):
    result = []

    def solve(old=-sys.maxsize, index=0):
        if index == len(arr):
            result.append(old)
            return True
        g = index + 1
        while g < len(arr) and int(arr[index:g]) < old:
            g += 1
        if len(arr[index:g]) != 0 and int(arr[index:g]) > old and solve(int(arr[index:g]), g):
            if old != -sys.maxsize:
                result.append(old)
            return True
        return False

    res = solve()
    print(result)
    return res


arr = "9012"
# arr = "1234"
print(find(arr))
