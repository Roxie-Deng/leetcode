# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Bottom -> BFS; Left: first one in the bottom row
        if root is None:
            return
        q = deque([root]) # deque() 需要可迭代对象（iterable）来初始化，等价于 q = deque() q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return level[0]

# O(n); O(n/2)