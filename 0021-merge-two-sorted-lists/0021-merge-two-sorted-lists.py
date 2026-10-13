# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        d = ListNode()
        cur = d
        while l1 and l2:
            x, y = l1.val, l2.val
            if x<y:
                cur.next=l1
                l1 = l1.next
            else:
                cur.next=l2
                l2 = l2.next
            cur = cur.next
        if l1: cur.next=l1
        else: cur.next=l2
        return d.next