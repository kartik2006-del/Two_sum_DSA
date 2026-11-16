# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        dummy=ListNode(0)
        dummy.next=head
        if not head:
            return None
        temp=dummy
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else :
                temp=temp.next
        return dummy.next       