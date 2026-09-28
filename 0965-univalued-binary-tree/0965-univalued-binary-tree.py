# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        def r(n):
            if not n: return 1==1
            return root.val==n.val and r(n.left) and r(n.right)
        return r(root)