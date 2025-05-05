# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]
        def maxDepth(root): 
            if root == None:
                return 0
            
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            diameter[0] = max(left+right,diameter[0])

            return 1+max(left, right)

        l = maxDepth(root)

        return diameter[0]
                
        