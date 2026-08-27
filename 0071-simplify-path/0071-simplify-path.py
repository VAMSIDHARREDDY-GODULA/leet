class Solution(object):
    def simplifyPath(self, path):
        x = []
        s = path.split('/')
        for i in s:
            if not i or i=='.':
                continue
            elif i=='..':
                if x: x.pop()
            else:x.append(i)
        return '/'+'/'.join(x) 