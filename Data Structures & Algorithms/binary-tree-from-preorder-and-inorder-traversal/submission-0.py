# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        new_node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        """
        # preorder must be same size and contain same elements as the inorder subtree
        For preorder = [3, 9, 20, 15, 7] and inorder = [9, 3, 15, 20, 7]:
        Root = 3 (first in preorder).
        inorder splits into [9] (left subtree) and [15, 20, 7] (right subtree).
        preorder splits into [9] (left subtree) and [20, 15, 7] (right subtree).
        """

        new_node.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        new_node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return new_node