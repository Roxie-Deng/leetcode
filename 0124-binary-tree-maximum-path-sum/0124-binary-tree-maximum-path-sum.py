# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 当前节点为顶端的单边最大路径和 = node.val + max(f(node.left),f(node.right))，递归向上返回这个值
        # 因为可以从任何节点出发，维护一个全局变量记录所有顶端路径和的最大值  = node.val + f(left) + f(right)

        self.cur_max = float('-inf')
        def dfs(node:Optional[TreeNode]) -> int:
            # 当前节点为顶端的单边最大路径和
            if node is None:
                return 0
            # 左右子树的单边贡献（负数直接丢弃）
            left = max(0, dfs(node.left)) 
            right = max(0,dfs(node.right))
            # nonlocal cur_max # 之前用的nonlocal是一个声明语句，不能和赋值写在同一行

            # 更新全局答案：以当前节点为顶端的完整路径（可以同时连接左右两边）
            self.cur_max =  max(self.cur_max, node.val + left + right)
            # 返回给父节点的单边贡献（只能选较大的那一边）
            return node.val + max(left,right)
        dfs(root)
        return self.cur_max
        # 递归深度logn, worst case一条链n
        # 每个节点被访问一次O(n);O(n)