# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        maxm = -float('inf')
        cnt = 0
        level = 0
        while q:
            temp = len(q)
            levelSum = 0
            cnt += 1
            for i in range(temp):
                curr = q.popleft()
                levelSum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if levelSum>maxm:
                maxm = levelSum
                level = cnt
        return level

        