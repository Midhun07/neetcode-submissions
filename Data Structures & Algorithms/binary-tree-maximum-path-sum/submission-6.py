# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # track maxsum. At every node get the sum of its left and right path and compare the maximum of (left, right, left+root, right+root and sum of all).
        self.maxsum = -float('inf')

        def find_sum(root):
            if root is None:
                return 0
            left = find_sum(root.left)
            right = find_sum(root.right)
            left_gain = max(0, left)
            right_gain = max(0, right)
            self.maxsum = max(self.maxsum, root.val + left_gain + right_gain)
            return root.val + max(left_gain, right_gain)
        find_sum(root)
        return self.maxsum