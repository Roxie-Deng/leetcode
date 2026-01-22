# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 等同于求左右子树最大深度和
        ans = 0
        # 以当前节点为根节点，返回左右子树最大深度，同时更新直径（左右子树最大深度和）
        def dfs(node) -> int:
            if node is None:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal ans # 引用全局变量ans
            ans = max(ans,l+r) # 更新ans

            return max(l,r)+1 #返回最大深度
        
        dfs(root)
        return ans
        # O(n);O(depth)