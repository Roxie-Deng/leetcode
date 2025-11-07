# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = -inf #上一个节点值
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 左树所有节点 < root <右树所有节点
        # 中序遍历：inorder(left) root inorder(right)
        # BST的中序遍历：must be an ascending seq, 当前节点值一定比上一个节点值要大

        if root is None:
            return True
        # visit left tree
        if not self.isValidBST(root.left):
            return False
        # visit root
        if root.val <= self.pre:
            return False

        # update state var
        self.pre = root.val
        # visit right tree
        return self.isValidBST(root.right)
            
        