# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        s = []
        def r(n):
            if not n: return 0
            if n:
                if not n.left and not n.right:
                    return n.val
            s.append(r(n.left))
            r(n.right)
        r(root)
        return sum(i for i in s if i)