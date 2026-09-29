# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        b = []
        def r(n):
            if not n: return
            r(n.left)
            b.append(n.val)
            r(n.right)
        r(root)
        a = float('inf')
        for i in range(len(b)-1):
            x = b[i+1]-b[i]
            if x<a:
                a = x
                if a==1: return a
        return a