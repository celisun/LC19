class Stack:  # pop heavy, read heavy, pop O(1) time, push O(n) itme
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        # 3 2 1
        # 4
        # 4 3 2 1
        #
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1: return -1
        return self.q1.pop(0)

    def top(self):
        return self.q1[0] if self.q1 else -1

# s = Stack()
# s.push(1)
# s.push(2)
# print (s.pop())
# s.push(3)
# print (s.pop())


class Stack2:  # push heavy, store value more than get access to it
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        # 1 2 3 4
        self.q1.append(x)

    def pop(self):
        if not self.q1: return
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))
        tmp = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1   # swap the name
        return tmp

    def top(self):
        tmp = self.pop()
        self.push(tmp)
        return tmp

s = Stack2()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print (s.top())
s.pop()
print (s.top())
s.pop()
print (s.top())