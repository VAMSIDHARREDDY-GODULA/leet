class Solution(object):
    def fizzBuzz(self, n):
        b = []
        for i in range(1,n+1):
            if not i%3 and not i%5:
                b.append('FizzBuzz')
            elif not i%3:
                b.append('Fizz')
            elif not i%5:
                b.append('Buzz')
            else:
                b.append(str(i))
        return b