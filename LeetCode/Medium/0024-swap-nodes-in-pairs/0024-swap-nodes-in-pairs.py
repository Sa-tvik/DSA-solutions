# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        slow, fast = head, head.next
        dummy = ListNode()
        dummy.next = fast
        prev = dummy
        while fast:
            prev.next = fast
            slow.next = fast.next
            fast.next = slow
            prev=slow

            slow = slow.next
            if slow and slow.next:
                fast = slow.next
            else:
                break

        return dummy.next


        return dummy.next
            


