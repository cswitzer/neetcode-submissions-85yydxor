# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            curr_dia = left + right
            self.max_dia = max(self.max_dia, curr_dia)
            return 1 + max(left, right)
        
        dfs(root)
        return self.max_dia
