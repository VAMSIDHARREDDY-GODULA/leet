# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        n = set(nums)
        while head.val in n:
            head = head.next
        c = head
        while c and c.next:
            if c.next.val in n:
                c.next = c.next.next
            else: c = c.next
        return head