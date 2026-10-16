class Solution(object):
    def largestOddNumber(self, num):
        b = ['9','7','5','3','1']
        for i, j in enumerate(num[::-1]):
            print(j in b,j)
            if j in b:
                return num[:len(num)-i]
        return ''