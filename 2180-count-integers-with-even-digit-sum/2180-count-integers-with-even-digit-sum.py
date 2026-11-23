class Solution(object):
    def countEven(self, num):
        a, n = 0, num
        while n:
            a += n%10
            n //= 10
        return (num-1)/2 if a%2 else num//2