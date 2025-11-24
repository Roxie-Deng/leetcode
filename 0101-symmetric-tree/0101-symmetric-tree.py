# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # p.left == q.right, p.right == q.left
        def dfs(p,q):
            if p is None or q is None:
                return p is q
            if p.val == q.val:
                return dfs(p.left,q.right) and dfs(p.right, q.left)
            return False
        
        return dfs(root.left,root.right)