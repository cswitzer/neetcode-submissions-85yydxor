# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = 0

        def dfs(curr: Optional[TreeNode]) -> None:
            # inorder traversal
            if not curr:
                return
            
            dfs(curr.left)

            self.k -= 1
            if self.k == 0:
                self.result = curr.val
                return

            dfs(curr.right)
        
        dfs(root)
        return self.result

