class Solution(object):
    def defangIPaddr(self, address):
        s = ''
        for i in address:
            if i!='.':
                s += i
            else:
                s += '[.]'
        return s