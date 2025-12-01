# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 基于BFS：取当前节点时，奇数层popleft,偶数层pop
        if root is None:
            return []
        ans = [] # 存储答案
        q = deque([root]) # 存储节点
        switch = True # 第一层从左边取

        while q:
            vals = [] # 存储当前层的节点值 
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if switch:
                ans.append(vals)
            else:
                ans.append(vals[::-1])
            switch = not switch
        
        return ans

        # O(n); O(width)->O(n/2)