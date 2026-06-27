# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root, left, right
        # inorder: left, root, right
        # preorder[0]-> ROOT
        # 找到inorder里的ROOT，左边的数都在左子树中，右边的数都在右子树中，可知左右子树大小，能再次对应preorder中的子数组
        # 再次得知左/右子树的inorder+preorder
        if not preorder:
            return None
        left_size = inorder.index(preorder[0]) # 获取root在inorder中的index
        left= self.buildTree(preorder[1:left_size+1],inorder[:left_size])#构建左子树
        right= self.buildTree(preorder[left_size+1:],inorder[left_size+1:])#构建右子树
        return TreeNode(preorder[0],left,right)
        # 链状O(n);每次查找inorder.index(preorder[0])和复制preorder[1:left_size+1] O(n)
        # time:O(n^2);space:O(n^2)