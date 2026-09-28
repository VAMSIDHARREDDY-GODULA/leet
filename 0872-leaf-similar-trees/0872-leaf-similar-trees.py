# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        def r(n,l):
            if n:
                if not n.left and not n.right:
                    l.append(n.val)
                r(n.left,l)
                r(n.right, l)
            return l
        return r(root1,[])==r(root2,[])