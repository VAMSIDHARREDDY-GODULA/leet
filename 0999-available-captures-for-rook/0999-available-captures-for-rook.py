class Solution(object):
    def numRookCaptures(self, b):
        c1 = c2 = c3 = c4 = x = 0
        m = n = 1
        for i in b:
            if 'R' in i:
                y = i.index('R')
                break
            x += 1
        for i in range(8):
            if i<x:
                if b[i][y]=='p':
                    c1 = 1 
                elif b[i][y]=='B':
                    c1 = 0
            if i>x and m:
                if b[i][y]=='p':
                    c2 = 1
                    m = 0
                elif b[i][y]=='B':
                    m = c2 = 0
            if i<y:
                if b[x][i]=='p':
                    c3 = 1 
                elif b[x][i]=='B':
                    c3 = 0
            if i>y and n:
                if b[x][i]=='p':
                    c4 = 1
                    n = 0
                elif b[x][i]=='B':
                    n = c4 = 0
        return c1+c2+c3+c4