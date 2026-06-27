# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    hook = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        nodes=[]
        # preorder: root, left, right
        def preorder(node:Optional[TreeNode]):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        # O(n);O(n)
        '''
        # 继续优化，Morris遍历：先找cur左子树的最右下角，将root的右子树接到后面； 再将root的左子树接到root.right位置，然后置空root.left
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right # 找右下角
                pre.right = cur.right # 把cur的右子树接到pre右边
                cur.right = cur.left # 把cur的左子树接到cur的右
                cur.left = None
            cur = cur.right