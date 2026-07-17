# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        # assuming we count the height by the number of nodes
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            left = self.height(node.left)
            right = self.height(node.right)
            is_currently_balanced = abs(left - right) <= 1
            
            # IF the current node is balanced, then we check if all the subnodes to the left
            # and the right are balanced as well
            return (
                is_currently_balanced and
                dfs(node.right) and
                dfs(node.left)
            )
        
        return dfs(root)
            
            