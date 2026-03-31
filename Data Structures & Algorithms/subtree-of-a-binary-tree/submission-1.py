# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            # None is always a subtree
            return True
        if not root:
            return False
        
        if self.is_same_tree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_same_tree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot and not root:
            return True
        
        if root and subroot and root.val == subroot.val:
            return self.is_same_tree(root.left, subroot.left) and self.is_same_tree(root.right, subroot.right)
        
        return False