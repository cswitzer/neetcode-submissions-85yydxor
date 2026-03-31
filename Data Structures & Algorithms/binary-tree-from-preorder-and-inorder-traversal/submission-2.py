# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # preorder tells me the current root. Finding the current root in the inorder tree essentially
        # splits the tree into left and right subtrees. By recursively solving left and right subtrees,
        # we can rebuild the tree
        new_node = TreeNode(val=preorder[0])
        part_idx = inorder.index(preorder[0])
        new_node.left = self.buildTree(preorder[1 : part_idx + 1], inorder[:part_idx])
        new_node.right = self.buildTree(preorder[part_idx + 1:], inorder[part_idx + 1:])
        return new_node