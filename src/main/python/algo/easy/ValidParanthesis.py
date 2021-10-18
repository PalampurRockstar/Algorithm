#https://leetcode.com/problems/valid-parentheses/

def solve_1(arr, S=[]):
    map = dict({'(': ['p', 1], ')': ['p', 2], '{': ['c', 1], '}': ['c', 2], '[': ['s', 1], ']': ['s', 2], })
    for v in arr:
        if v in map:
            if not S:
                S.append(map[v])
            elif map[v][1] == 1:
                S.append(map[v])
            elif map[v][0] == S[-1][0] and S[-1][1] == 1:
                S.pop()
            else:
                return False
        else:
            return False
    return True if len(S) == 0 else False


def solve_2(arr, S=[], map=dict({'(': ')', '{': '}', '[': ']'})):
    for v in arr:
        if v in map:
            S.append(map[v])
        elif not S or S.pop() != v:
            return False
    return True if len(S) == 0 else False


print(solve_1("{[]}"))
print(solve_1("))"))

print(solve_2("{[]}"))
print(solve_2("))"))
