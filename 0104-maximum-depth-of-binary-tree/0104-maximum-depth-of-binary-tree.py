# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        q = deque([root])
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                n = q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
        return d