def find(input):
    length = len(input)
    if length == 0: return []
    prev = input[0]
    count = 1
    result = []
    for i in input[1:]:
        if i != prev:
            result.append(str(count) + prev)
            prev = i
            count = 0
        count += 1
    result.append(str(count) + prev)
    return result


input = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'a']
print(find(input))
