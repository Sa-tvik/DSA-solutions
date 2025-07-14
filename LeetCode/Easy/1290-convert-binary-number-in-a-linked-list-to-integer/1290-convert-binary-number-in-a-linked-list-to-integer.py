# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0)  
            res, mult = helper(node.next)
            return ((2 ** mult) * node.val + res, mult + 1)

        return helper(head)[0]