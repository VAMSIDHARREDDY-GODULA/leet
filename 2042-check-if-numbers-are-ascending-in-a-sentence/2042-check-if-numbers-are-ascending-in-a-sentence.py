class Solution(object):
    def areNumbersAscending(self, s):
        z = 0
        for i in s.split():
            if i.isdigit():
                if z>=int(i): return 1==2
                z = int(i)
        return 1==1