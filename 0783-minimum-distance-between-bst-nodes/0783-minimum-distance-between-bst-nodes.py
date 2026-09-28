# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        b = []
        def r(n,):
            if not n: return
            r(n.left)
            b.append(n.val)
            r(n.right)
            return b
        s = r(root)
        a = float('inf')
        for i in range(len(s)-1):
            x = s[i+1]-s[i]
            if x<a: a=x
        return a