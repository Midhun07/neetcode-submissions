# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bst(self, l1, l2, pos):
        node = None
        if l1 and l2:
            v = l1.pop(0)
            ind = pos[v] - pos[l2[0]]
            left = self.bst(l1, l2[:ind], pos)
            right = self.bst(l1, l2[ind+1:], pos)
            node = TreeNode(v, left, right)
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v:i for i, v in enumerate(inorder)}
        return self.bst(preorder, inorder, pos)