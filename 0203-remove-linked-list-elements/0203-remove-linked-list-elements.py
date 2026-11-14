# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        if not head:
            return None
        dummy_node=ListNode(0)
        dummy_node.next=head
        temp=dummy_node
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return dummy_node.next

                
            

                