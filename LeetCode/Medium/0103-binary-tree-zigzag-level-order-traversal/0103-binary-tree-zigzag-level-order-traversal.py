# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque()
        reverse = False
        res = []
        dq.append(root)
        while dq:
            level = []
            for _ in range(len(dq)):
                if not reverse:
                    temp = dq.popleft()
                    level.append(temp.val)
                    if temp.left:
                        dq.append(temp.left)
                    if temp.right:
                        dq.append(temp.right)
                else:
                    temp = dq.pop()
                    level.append(temp.val)
                    if temp.right:
                        dq.appendleft(temp.right)
                    if temp.left:
                        dq.appendleft(temp.left)
            reverse = not reverse
            res.append(level)
        return res

