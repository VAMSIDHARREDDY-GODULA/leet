class Solution(object):
    def minOperations(self, logs):
        x = []
        for i in logs:
            if i not in ['./','../','x/']:
                x.append(i)
            elif i=='../':
                if x:
                    x.pop()
        return len(x)