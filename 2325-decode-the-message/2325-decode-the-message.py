class Solution(object):
    def decodeMessage(self, key, message):
        k = key.replace(' ','')
        d = {' ':' '}
        l = ord('a')
        for i in k:
            if i not in d:
                d[i]=chr(l)
                l += 1
            if len(d)==27: break
        t = ''
        for i in message:
            t += d[i]
        return t