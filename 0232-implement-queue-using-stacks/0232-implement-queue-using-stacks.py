class MyQueue(object):

    def __init__(self):
        self.q = []
        self.s = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        if not self.s:
            while self.q:
                self.s.append(self.q.pop())
        return self.s.pop()

    def peek(self):
        if not self.s:
            while self.q:
                self.s.append(self.q.pop())
        return self.s[-1]

    def empty(self):
        return not self.s and not self.q


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()