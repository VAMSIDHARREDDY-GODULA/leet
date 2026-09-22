class Solution(object):
    def maximum69Number (self, num):
        if '6' not in str(num):
            return num
        x = list(str(num))
        for i in range(len(x)):
            if x[i]=='6':
                x[i] = '9'
                break
        return int(''.join(x))