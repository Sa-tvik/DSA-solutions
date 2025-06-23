# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        def helper(node, dist):
            if node == None:
                return -1
            
            if node == target:
                collect(node,0)
                return 0
            
            left = helper(node.left, dist)
            if left!=-1:
                if left + 1 == k:
                    res.append(node.val)
                else:
                    collect(node.right, left+2)
                return left+1

            right = helper(node.right, dist)  
            if right!=-1:
                if right + 1 == k:
                    res.append(node.val)
                else:
                    collect(node.left, right+2)
                return right+1
            return -1

        def collect(node, dist):
            if node is None:
                return
            if dist == k:
                res.append(node.val)
                return
            collect(node.left, dist + 1)
            collect(node.right, dist + 1)
        
        helper(root, 0)
        return res
