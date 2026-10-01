class Solution(object):
    def average(self, salary):
        t = sum(salary)-min(salary)-max(salary)
        t = round(float(t)/(len(salary)-2),5)
        return t