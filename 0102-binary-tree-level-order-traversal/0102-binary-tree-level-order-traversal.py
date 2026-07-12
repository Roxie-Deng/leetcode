# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        ans = []

        if root is None:
            return ans

        # 分层处理，用队列最为合适，队首取出该层节点，队尾添加下层节点
        dq = deque([root])

        while dq:
            level = [] # 每层需要一个答案容器

            # 出队
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val) # 记录答案
                if node.left: dq.append(node.left) 
                if node.right: dq.append(node.right) 

            # 入队
            ans.append(level)
        return ans
        # O(n); O(max_width) = O(n/2)
