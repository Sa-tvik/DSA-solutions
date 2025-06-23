# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def rightHeight(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        def count(node):
            if not node:
                return 0

            lh = leftHeight(node)
            rh = rightHeight(node)

            if lh == rh:
                return 2**lh - 1 
            else:
                return 1 + count(node.left) + count(node.right)

        return count(root)