# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.preorder: list[str] = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                self.preorder.append("N")
                return
            
            self.preorder.append(str(root.val))
            root.left = dfs(root.left)
            root.right = dfs(root.right)
        
        dfs(root)
        return ",".join(self.preorder)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        vals = iter(data.split(","))
        def dfs() -> Optional[TreeNode]:
            val = next(vals)
            if val == "N":
                return None
            
            new_node = TreeNode(int(val))
            new_node.left = dfs()
            new_node.right = dfs()
            return new_node
        
        return dfs()
