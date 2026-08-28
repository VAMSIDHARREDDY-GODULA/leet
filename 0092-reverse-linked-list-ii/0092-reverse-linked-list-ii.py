# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left==right:
            return head
        cu = c = head
        x = []
        l, r = left, right
        while cu:
            right -= 1
            left -= 1
            if left<1:x.append(cu.val)
            if not right: break
            cu = cu.next
        while x:
            l -= 1
            if l<1:
                c.val = x.pop()
            c = c.next
        return head