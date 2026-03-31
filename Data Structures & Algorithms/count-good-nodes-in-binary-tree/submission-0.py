# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def dfs(curr_node: Optional[TreeNode], max_so_far: int = -101):
            if not curr_node:
                return
            
            # preorder traversal
            if curr_node.val >= max_so_far:
                self.good_nodes += 1
                max_so_far = curr_node.val
            
            dfs(curr_node.left, max_so_far)
            dfs(curr_node.right, max_so_far)

        dfs(root)
        return self.good_nodes