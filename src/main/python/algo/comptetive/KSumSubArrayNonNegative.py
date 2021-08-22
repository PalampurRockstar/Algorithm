def find(arr, k, acc=0, ps=dict({0: -1}), res=[]):
    for i, v in enumerate(arr):
        acc += v
        ps[acc] = i
        if acc - k in ps: res.append(arr[ps[acc - k] + 1:i + 1])
    return res


arr = [1, 4, 20, 3, 10, 5]
print(find(arr, 33))
