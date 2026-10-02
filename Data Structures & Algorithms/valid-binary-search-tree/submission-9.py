from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, -1000000001, 1000000001)])
        while queue:
            for _ in range(len(queue)):
                node, lb, ub = queue.popleft()
                if lb < node.val < ub:
                    if node.left:
                        queue.append((node.left, lb, node.val))
                    if node.right:
                        queue.append((node.right, node.val, ub))
                else:
                    return False
        return True
                