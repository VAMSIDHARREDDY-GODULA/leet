# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        b, c = {}, []
        def r(n):
            if not n: return
            r(n.left)
            x = n.val
            if x in b: b[x] += 1
            else: b[x] = 1
            r(n.right)
        r(root)
        m = max(b.values())
        for i in b:
            if b[i]==m: c.append(i)
        return c