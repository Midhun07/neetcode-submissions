class Solution:
    def __init__(self):
        self.counter = 0
        self.kele = 10001

    def kst(self, root, k):
        if not root:
            return

        if root.left:
            self.kst(root.left, k)
        self.counter -= 1
        if not self.counter:
            self.kele = root.val
        if root.right:
            self.kst(root.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Since it is a BST, a dfs approach is better since the left nodes are always the lowest. Keep pushing elements to the stack untill it reaches the K+1 length and then pop the last element.
        self.counter = k
        self.kst(root, k)
        return self.kele
        
        