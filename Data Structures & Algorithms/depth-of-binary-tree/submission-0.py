# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        if root:
            dl = self.maxDepth(root.left)
            dr = self.maxDepth(root.right)
            self.depth = max(dl, dr) + 1
        
        return self.depth
        