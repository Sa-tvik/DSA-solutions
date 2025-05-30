# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if root == None:
            return root

        newNode = TreeNode(root.val)
        def invert(node):
            if node == None:
                return
            
            newNode = TreeNode(node.val)
            newNode.right = invert(node.left)
            newNode.left = invert(node.right)

            return newNode

        return invert(root)

        