arr = [18, 19, 29, 15, 16]


class MinStack:

    def __init__(self):
        self.S = []
        self.min = 0

    def push(self, n):
        if self.S:
            if self.min < n:
                self.S.append(n)
            else:
                self.S.append((2 * n) - self.min)
                self.min = n

        else:
            self.S.append(n)
            self.min = n

    def pop(self):
        if self.S:
            if self.S[-1] < self.min:
                poped = self.min
                self.min = (2 * self.min) - self.S[-1]
                self.S.pop()
                return poped
            else:
                return self.S.pop()
        else:
            return -1

    def min_el(self):
        if self.S:
            return self.min
        else:
            return -1

    def top(self):
        if self.S:
            return max(self.S[-1], self.min)
        else:
            return -1


ms = MinStack()
# ms.push(18)
# ms.push(19)
# print("MIN : " + str(ms.min_el()))
# ms.push(29)
# print("MIN : " + str(ms.min_el()))
# print("TOP : " + str(ms.top()))
# ms.push(15)
# print("MIN : " + str(ms.min_el()))
# print("TOP : " + str(ms.top()))
# ms.push(16)
# print("MIN : " + str(ms.min_el()))
# print("TOP : " + str(ms.top()))
# print("---")
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))
# print("POP : " + str(ms.pop()))

ms.push(3)
ms.push(5)
print("MIN : " + str(ms.min_el()))
ms.push(2)
ms.push(1)
print("MIN : " + str(ms.min_el()))
print("POP : " + str(ms.pop()))
print("MIN : " + str(ms.min_el()))
print("POP : " + str(ms.pop()))
print("TOP : " + str(ms.top()))
