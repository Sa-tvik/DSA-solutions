# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr = head.next
        prev = head
        temp = head
        while curr:
            if prev.val==curr.val:
                curr = curr.next
                continue
            else:
                prev.next = curr
                prev = prev.next
            temp = curr
            curr = curr.next
        if prev.val == temp.val:
            prev.next = None
        return head
            