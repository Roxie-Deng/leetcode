# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # all possible paths -> 递归
        prefix = defaultdict(int)# 前缀和出现的次数
        prefix[0] = 1
        def dfs(node, cur_sum)-> int: # 节点，根节点到该节点的和 -> 可能路径数
            if not node:
                return 0 
            cur_sum += node.val
            res = prefix.get(cur_sum-targetSum,0) # 是否存在old_sum满足cur_sum-old_sum = target_sum，这个old_sum出现了多少次
            prefix[cur_sum] += 1

            res += dfs(node.left,cur_sum)# 加入左子树的路径数
            res += dfs(node.right,cur_sum)
            prefix[cur_sum] -= 1 # 离开当前节点，返回到父节点，prefix记录“当前正在递归的路径”上的前缀和。它已经不在我们能看到路径上了，这个节点到根节点的前缀和在字典中应该消失掉

            return res
        return dfs(root,0)
        # O(n);O(n)
