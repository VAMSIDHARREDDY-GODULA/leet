class Solution(object):
    def modifyString(self, s):
        if '?' not in s: return s
        elif '?'==s: return 'a'
        s = list(s)
        while '?' in s:
            x = s.index('?')
            if not x:
                if s[x+1]!='a': s[x]='a'
                else: s[x]='b'
            elif x==len(s)-1:
                if s[x-1]!='a': s[x]='a'
                else: s[x]='b'
            else:
                if s[x-1]!='a' and s[x+1]!='a': s[x]='a'
                elif s[x-1]!='b' and s[x+1]!='b': s[x]='b'
                elif s[x-1]!='c' and s[x+1]!='c': s[x]='c'
                else: s[x]='a'
        return ''.join(s)