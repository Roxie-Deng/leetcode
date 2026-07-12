# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # left = right, left.left = right.right,left.right = right.left
        # 左树: left-root-right, 右树:right-root,left
        l_tree = root.left
        r_tree = root.right
        
        def dfs(node1, node2):
            if not node1 or not node2:
                return node1 == node2
                # 节点 or 节点，if False, 跳过
                # 节点 or None, if True, return False
                # None or None, if True, return True
            if node1.val != node2.val: # 两个节点，值不相等
                return False
            
            # 两个节点，值相等，这才进入下一层
            return dfs(node1.left,node2.right) and dfs(node1.right,node2.left)

        return dfs(l_tree,r_tree)
        # O(n);O(n),平均log(n)