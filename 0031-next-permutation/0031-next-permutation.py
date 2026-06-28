class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 字典序
        # 1.从右往左找 第一个“左边<右边”的位置i（左边）
        # (如果找到了说明在i+1后面的是递减)
        # 2.然后从右往左找 最小的比nums[i]大的数 的位置j （其实也就是第一个比nums[i]大的）
        # 3.交换它们
        # 4.（i+1后面的是递减）把它变为升序，反转nums[i+1:]
        # 1，3，4，2
        # 1, 4, 3, 2
        # 1, 4, 2, 3
        n = len(nums)
        i = n-2

        while i>=0 and nums[i]>=nums[i+1]:
            i -= 1 # 没找到左<右，i继续左移

        # 找到了i。继续找j使得nums[j]>nums[i]
        if i>=0:
            j = n-1
            while nums[j]<=nums[i]:
                j -= 1
            # 找到j
            nums[i],nums[j] = nums[j],nums[i]
        
        # 反转nums[i+1:]
        # 如果没有找到i，那么整个nums都是降序的，循环到最小的排列顺序，整个颠倒 
        left = i+1
        right = n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        # O(n);O(1)