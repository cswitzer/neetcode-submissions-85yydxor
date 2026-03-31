# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(root):
            nonlocal max_path_sum
            if not root:
                return 0

            # if a child subtree contributes a negative sum, it is better not to take it at all
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            
            # What is the best (max) path that passes through me
            max_path_sum = max(max_path_sum, root.val + left + right)

            # What is the best path extending upwards
            return root.val + max(left, right)

        dfs(root)
        return max_path_sum