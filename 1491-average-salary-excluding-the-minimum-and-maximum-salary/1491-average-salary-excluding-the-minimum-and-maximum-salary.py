class Solution(object):
    def average(self, salary):
        t = sum(salary)-min(salary)-max(salary)
        return float(t)/(len(salary)-2)