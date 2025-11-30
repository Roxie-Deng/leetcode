# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root]) # 存储待访问的节点，root作为第一个待访问的节点

        while q:
            vals = [] # 存储节点值
            for _ in range(len(q)): # 当前层的节点数
                # 从队列中取出当前层节点
                node = q.popleft()
                vals.append(node.val)
                # 把下一层节点加入队列
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals)
        return ans