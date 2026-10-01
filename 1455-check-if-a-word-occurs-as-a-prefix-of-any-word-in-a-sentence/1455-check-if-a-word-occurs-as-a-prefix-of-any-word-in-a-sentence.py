class Solution(object):
    def isPrefixOfWord(self, sen, sea):
        for j,i in enumerate(sen.split()):
            if sea==i[:len(sea)]: return j+1
        return -1