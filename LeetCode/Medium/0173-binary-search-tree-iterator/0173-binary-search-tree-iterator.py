# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.st = deque()
        self.pushAll(root)
    def pushAll(self, root):
        while root!=None:
            self.st.append(root)
            root = root.left
        return

    def next(self) -> int:
        temp = self.st.pop()
        self.pushAll(temp.right)
        return temp.val

    def hasNext(self) -> bool:
        return len(self.st)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()