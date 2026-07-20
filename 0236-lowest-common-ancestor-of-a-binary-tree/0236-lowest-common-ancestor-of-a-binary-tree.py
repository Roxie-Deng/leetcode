# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # brutal: 记录root走到p的路径，再记录root走到q的路径，对比，最后一个相同的节点即是答案
        # 转化为 当前节点root是不是lowestCommonAncestor的问题：站在当前节点，去左右子树里找p or q, 如果左子树/右子树各有一个p/q, 那么当前节点就是答案； p/q都在一侧，那就走到root.left(or root.right)再看 -> 递归
        
        def dfs(node: 'TreeNode'):
            if node is p or node is q or node is None:
                return node # 找到p，找到q，没找到
            
            left = dfs(node.left) # p or q or None
            right = dfs(node.right) # p or q or None

            if left and right: # 都不是None
                return node # 找到答案

            return left or right # 递归
        
        return dfs(root)
        # O(n);O(n)

            