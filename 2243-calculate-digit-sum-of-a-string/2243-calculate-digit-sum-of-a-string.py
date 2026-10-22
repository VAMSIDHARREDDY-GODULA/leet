class Solution(object):
    def digitSum(self, s, k):
        while len(s)>k:
            z = ''
            for i in range(0,len(s),k):
                x = 0
                j = i
                while j<i+k and j<len(s):
                    x += int(s[j])
                    j += 1
                z += str(x)
            s = z
        return s