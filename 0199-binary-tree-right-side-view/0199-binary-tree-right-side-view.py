# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 记录每一层最右的节点，先右后左
        ans = []
        def dfs(node,depth): # 当前节点和所在层
            if node is None:
                return
            if depth == len(ans):
                ans.append(node.val)
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        dfs(root,0)
        return ans
    # O(n);O(depth)