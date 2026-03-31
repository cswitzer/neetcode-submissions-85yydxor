# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root:
            return result

        q = deque()
        q.append(root)

        while q:
            level = []
            q_len = len(q)
            for _ in range(q_len):
                curr = q.popleft()
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            result.append(level[-1])
        return result