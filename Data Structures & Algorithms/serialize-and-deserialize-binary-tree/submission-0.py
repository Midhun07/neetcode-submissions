# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []
        def dfs(root):
            if root is None:
                string.append("#")
                return
            string.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = ",".join(string)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        string = iter(data.split(","))
        def dfs():
            item = next(string)
            if item == "#":
                return None
            node = TreeNode(int(item))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()