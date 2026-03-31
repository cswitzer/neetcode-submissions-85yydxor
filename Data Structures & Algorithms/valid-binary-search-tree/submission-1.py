# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], lower_bound: int, upper_bound: int):
            if not root:
                return True
            
            if not lower_bound < root.val < upper_bound:
                return False
            
            return dfs(root.left, lower_bound, root.val) and dfs(root.right, root.val, upper_bound)
        
        return dfs(root, lower_bound=float("-inf"), upper_bound=float("inf"))