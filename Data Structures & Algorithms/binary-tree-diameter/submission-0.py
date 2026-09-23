# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    def get_dd(self, root):
        depth = 0
        if root:
            dl = self.get_dd(root.left)
            dr = self.get_dd(root.right)
            depth = max(dl , dr) + 1
            self.diameter = max(self.diameter, dl + dr)
        return depth
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _ = self.get_dd(root)
        return self.diameter