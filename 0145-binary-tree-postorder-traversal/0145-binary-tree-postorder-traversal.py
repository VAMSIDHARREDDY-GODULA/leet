# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        b = []
        def r(n):
            if not n:
                return
            r(n.left)
            r(n.right)
            b.append(n.val)
        r(root)
        return b