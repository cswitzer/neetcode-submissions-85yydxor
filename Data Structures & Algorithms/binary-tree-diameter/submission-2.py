class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter

    def dfs(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)

        diameter = left_height + right_height
        self.max_diameter = max(self.max_diameter, diameter)

        return 1 + max(left_height, right_height)