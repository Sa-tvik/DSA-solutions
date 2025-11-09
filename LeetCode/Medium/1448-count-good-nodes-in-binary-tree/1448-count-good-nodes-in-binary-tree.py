# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxm):
            if not node:
                return 0
            ans = 0
            if node.val>=maxm:
                ans +=1
                maxm = node.val
            
            left = helper(node.left, maxm)
            right = helper(node.right, maxm)

            return left + right + ans
        
        return helper(root, -float('inf'))
            