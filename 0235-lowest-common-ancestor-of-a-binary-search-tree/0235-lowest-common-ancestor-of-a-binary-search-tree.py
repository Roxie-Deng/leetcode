# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if p.val < x and q.val < x:  # p 和 q 都在左子树
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > x and q.val > x:  # p 和 q 都在右子树
            return self.lowestCommonAncestor(root.right, p, q)
        return root  # 其它