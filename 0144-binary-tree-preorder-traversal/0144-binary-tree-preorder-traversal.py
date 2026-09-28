# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        b = []
        def p(r,b):
            if r: b.append(r.val)
            else: return b
            p(r.left,b)
            p(r.right,b)
        p(root,b)
        return b