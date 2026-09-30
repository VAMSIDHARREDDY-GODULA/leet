class Solution(object):
    def stringMatching(self, w):
        b = []
        for i in range(len(w)-1):
            for j in range(i+1,len(w)):
                if w[i] not  in b and w[i] in w[j]: b.append(w[i])
                elif w[j] not in b and w[j] in w[i]: b.append(w[j])
        return b