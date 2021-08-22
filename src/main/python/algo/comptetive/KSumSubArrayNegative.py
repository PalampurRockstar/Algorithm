def find(arr, k, ps=dict({0: [-1]}), acc=0, res=[]):
    for i, v in enumerate(arr):
        acc += v
        if acc in ps:
            app = ps[acc]
            app.append(i)
        else:
            ps[acc] = [i]
        if acc - k in ps:
            for e in ps[acc - k]:
                res.append(arr[e + 1:i + 1])
    return res


arr = [10, 2, -2, -20, 10]
print(find(arr, -10))
