# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def c(n,m):
            if n and m:
                return n.val==m.val and c(n.left, m.right) and c(n.right, m.left)
            elif not n and not m: return True
            return False
        return c(root.left, root.right)