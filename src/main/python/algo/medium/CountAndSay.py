# https://leetcode.com/problems/count-and-say


def solve(n):
    answer = [[1]]
    for i in range(1, n):
        old = answer[-1]
        count = 1
        another = []
        for i in range(len(old)):
            if i + 1 < len(old) and old[i] == old[i + 1]:
                count += 1
            else:
                another.append(count)
                another.append(old[i])
                count=1
        answer.append(another)
    return "".join([str(e) for e in answer[- 1]])


for i in range(10):
    print(solve(i + 1))
