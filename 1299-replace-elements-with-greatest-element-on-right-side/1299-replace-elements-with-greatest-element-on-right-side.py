class Solution(object):
    def replaceElements(self, arr):
        a = 0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>a: a = arr[i]
            else: arr[i]=a
        arr.append(-1)
        return arr[1:]