# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # BST:left<root<right
        # 进行in-order中序遍历
        ans = []
        def traverse(node: Optional[TreeNode]):
            if node is None:
                return None
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        
        traverse(root)
        # 理论上ans已从小到大排列
        return ans[k-1]