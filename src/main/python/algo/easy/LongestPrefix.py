def find(arr, res=[]):
    arr.sort()
    for i in range(min(len(arr[0]), len(arr[-1]))):
        if arr[0][i] == arr[-1][i]:res.append(arr[0][i])
        else:break
    return "".join(res)


strs = ["flower", "flow", "flight"]
print(find(strs))
