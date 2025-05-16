# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, maxm):
            if node is None:
                return 0

            count = 1 if node.val >= maxm else 0
            maxm = max(maxm, node.val)

            count += helper(node.left, maxm)
            count += helper(node.right, maxm)

            return count

        return helper(root, root.val)