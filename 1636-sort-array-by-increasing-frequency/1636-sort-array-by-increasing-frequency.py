class Solution(object):
    def frequencySort(self, nums):
        d, s = {}, []
        for i in set(nums):
            print(i)
            x = nums.count(i)
            if x in d: d[x].append(i)
            else:
                d[x]=[i]
                s.append(x)
            d[x].sort()
        l = 0
        s.sort()
        for i in s:
            for j in d[i][::-1]:
                x = i
                while x:
                    nums[l]=j
                    l += 1
                    x -= 1
        return nums
