class Solution(object):
    def interpret(self, c):
        return c.replace('()', 'o').replace('(al)','al')