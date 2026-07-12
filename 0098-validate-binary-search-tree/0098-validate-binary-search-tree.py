# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left<root<right
        # 天然成为一个inorder
        # 并且不是只比较一层，左子树所有节点都得比root小，右子树都比root大
        # -inf<左子树<root<右子树<inf

        # 左:-inf<node.left<node.val,右: 上一层node.val<node.right<inf
        # 设计三个变量
        def dfs(low:int,node:Optional[TreeNode],high:int) -> bool:
            if node is None:
                return True
            if not(low<node.val<high):
                return False
            
            return dfs(low,node.left,node.val) and dfs(node.val,node.right,high)

        return dfs(float('-inf'), root, float('inf'))
        # O(n);O(n)
        # dfs(root.left,root.right) 这种双参数一般用于对称/相同树