class Solution(object):
    def maximum69Number (self, num):
        if '6' not in str(num): return num
        i = str(num).find('6')
        x = list(str(num))
        x[i] = '9'
        return int(''.join(x))