class Solution(object):
    def maximum69Number (self, num):
        x = str(num)
        if '6' not in x: return num
        i = x.find('6')
        x = list(x)
        x[i] = '9'
        return int(''.join(x))