# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            left = self.height(root.left)
            right = self.height(root.right)
            balance_factor = abs(left - right)
            if balance_factor > 1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        is_balanced = depth(root)
        return is_balanced
    
    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))