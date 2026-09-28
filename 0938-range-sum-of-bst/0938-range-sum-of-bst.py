# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        def r(n):
            if not n: return 0
            if n.val<low: return r(n.right)
            elif n.val>high: return r(n.left)
            return n.val+r(n.left)+r(n.right)
        return r(root)