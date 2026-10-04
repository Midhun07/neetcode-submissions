# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v:i for i, v in enumerate(inorder)}
        self.idx = 0

        def helper(start, end):
            node = None
            if start <= end:
                val = preorder[self.idx]
                mid = pos[val]
                self.idx += 1
                node = TreeNode(val, None, None)

                node.left = helper(start, mid - 1)
                node.right = helper(mid + 1, end)
            return node
        
        return helper(0, len(inorder)-1)