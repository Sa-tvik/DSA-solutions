# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        if head == None or head.next == None: return head

        dummy = ListNode(-200)
        dummy.next = head
        temp = dummy
        curr = head
        prev = dummy
        while curr and curr.val<x:
                curr= curr.next
                temp = temp.next
        while curr:
            if curr.val>=x:
                prev = curr
                curr = curr.next
            else:
                prev.next = curr.next
                # prev = prev.next
                temp1 = curr
                curr = curr.next
                temp1.next = temp.next
                temp.next = temp1
                temp = temp1

        return dummy.next
                

                
                
        