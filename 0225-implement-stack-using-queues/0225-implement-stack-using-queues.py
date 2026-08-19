from collections import deque
class MyStack(object):
    def __init__(self):
        self.s = deque()        

    def push(self, x):
        self.s.append(x)
        n = len(self.s)
        while n>1:
            self.s.append(self.s.popleft())
            n -= 1

    def pop(self):
        return self.s.popleft()
        

    def top(self):
        return self.s[0]

    def empty(self):
        return len(self.s)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()