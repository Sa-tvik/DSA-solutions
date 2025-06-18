# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(placement,level, root, dic):
            if(not root):
                return
            dic[level].append((placement, root.val))
            helper(2*placement, level+1, root.left, dic)
            helper(2*placement+1, level+1, root.right, dic)

        dic = defaultdict(list)
        helper(1,0, root, dic)

        maxm = 0
        for level in dic:
            temp = dic[level]
            width = temp[-1][0] - temp[0][0] + 1
            maxm = max(maxm, width)

        return maxm
            
