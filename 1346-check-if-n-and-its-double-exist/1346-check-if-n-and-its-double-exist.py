class Solution(object):
    def checkIfExist(self, arr):
        b = set()
        for i in arr:
            if i*2 in b or not i%2 and i//2 in b:
                return True
            b.add(i)
        return False