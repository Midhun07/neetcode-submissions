# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.same = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                # print("1")
                self.same = False
                return self.same
            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)
        elif (p and (q is None)) or ((p is None) and q):
            # print("2")
            self.same = False
            return self.same
        else:
            self.same = self.same
        return self.same