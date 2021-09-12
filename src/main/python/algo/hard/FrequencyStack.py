class FreqStack:
    stack = []
    freq = dict();

    def push(self, el):
        if el in self.freq:
            self.freq[el] += 1
        else:
            self.freq[el] = 1

        if len(self.stack) < self.freq[el]:
            self.stack.append([el])
        else:
            self.stack[self.freq[el] - 1].append(el)

    def pop(self):
        if len(self.stack) == 0: return None
        if len(self.stack[-1]) > 1:
            el = self.stack[-1].pop()
            self.freq[el] -= 1
            return el
        else:
            el = self.stack[-1].pop()
            self.stack.pop()
            self.freq[el] -= 1
            return el


fs = FreqStack()
# fs.push(5)
# fs.push(7)
# fs.push(5)
# fs.push(7)
# fs.push(4)
# fs.push(5)

fs.push(5)
fs.push(1)
fs.push(2)
fs.push(5)
fs.push(5)
fs.push(5)
fs.push(1)
fs.push(6)
fs.push(1)
fs.push(5)

print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
print(fs.pop())
