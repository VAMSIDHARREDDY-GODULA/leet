# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, l):
        b = []
        for i in l:
            x = i
            while x:
                b.append(x.val)
                x = x.next
        b.sort()
        head = ListNode(0)
        cur = head
        for i in b:
            cur.next = ListNode(i)
            cur = cur.next
        return head.next