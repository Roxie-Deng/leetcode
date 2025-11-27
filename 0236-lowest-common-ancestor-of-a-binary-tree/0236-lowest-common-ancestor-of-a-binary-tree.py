# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 当前节点：1.为空 2.为p 3.为q -> 返回当前节点
        if root == None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q) # 左子树搜索结果: None 或某节点
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # 左右都不为None，当前节点为最近公共祖先
            return root
        if left: # 只有左边不为None，继续在左边搜索
            return left 
        return right # 否则继续在右边搜索

        # O(n);O(n)