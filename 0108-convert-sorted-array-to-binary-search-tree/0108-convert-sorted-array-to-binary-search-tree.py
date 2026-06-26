# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # BST: 左子树 < 根节点 < 右子树
        # input是有序数组，中间节点天然是BST根节点，然后再分别将左右subarry 排序为 tree，不断地重复子问题
        # mid; divide and conquer
        '''
        if not nums:
            return None
        m = len(nums)//2
        left = self.sortedArrayToBST(nums[:m])
        right = self.sortedArrayToBST(nums[m+1:])
        return TreeNode(nums[m],left,right) 
        # 递归深度logn，复制数组n O(nlogn);O(nlogn)
        '''
        # 继续优化：消除每次切片复制复杂度,记录上下限角标
        def dfs(l:int,r:int) -> Optional[TreeNode]: # [l,r]区间,返回root
            if l>r:
                return None
            m = (l+r)//2
            # TreeNode(val,left,right)
            root = TreeNode(nums[m], dfs(l,m-1), dfs(m+1,r))
            return root
        return dfs(0,len(nums)-1)
        # time: size(tree)=size(arr)，并且每个节点只被处理一次 O(n)
        # “层数（log n）”只有在“每一层都在做全局扫描或复制”时，才会乘到时间里去。如果每一层只是在创建单个节点，那“层数”这个数字就只配出现在空间（递归栈）里，绝对不准乘到时间上。
        # space: 递归深度O(logn)
