# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.status = True
    def check(self, root):
        depth = 0
        if root:
            dl = self.check(root.left)
            dr = self.check(root.right)
            depth = max(dl, dr) + 1
            self.status &= abs(dl - dr) <= 1
        return depth

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _ = self.check(root)
        return self.status