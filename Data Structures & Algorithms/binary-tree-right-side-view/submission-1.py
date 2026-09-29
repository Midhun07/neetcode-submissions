# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bfs(self, root):
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            read_right = False
            for i in range(len(queue)):
                if not read_right:
                    node = queue[-1]
                    res.append(node.val)
                    read_right = True
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.bfs(root)