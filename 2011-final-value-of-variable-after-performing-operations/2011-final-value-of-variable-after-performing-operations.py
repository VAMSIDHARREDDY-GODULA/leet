class Solution(object):
    def finalValueAfterOperations(self, o):
        x = 0
        for i in o:
            if '+' in i: x+=1
            else: x-=1
        return x