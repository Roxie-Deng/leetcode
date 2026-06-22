class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # in-place; no sorting
        # 把0全部换到1左边，2换到1右边
        # 遍历计数:cnt0,cnt1,cnt2,然后原地修改nums
        # range(0,cnt0),range(cnt0,n-cnt2),range(n-1-cnt2,n)
        # 继续优化：一边遍历一边计数0和2个数移动边界，并交换0到前面,2到后面,直至遍历到第一个2
        # 维护两个指针left(cnt0)和right(n-1-cnt2),cnt0,cnt2从0开始->left和right从两端开始

        n = len(nums)
        left,right = 0,n-1
        i = 0

        while i<=right: 
            if nums[i] > 1:
                nums[i],nums[right] = nums[right],nums[i]
                right -= 1
                # 需要检查新nums[i],因为不确定其与1的大小关系;i不能+1
            elif nums[i] < 1:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
                i += 1 
                # [left,i)都看过了,确保都<1,直接看下一个
            else:
                i += 1 # 若为1继续往后遍历
        return nums

        # O(n);O(1)