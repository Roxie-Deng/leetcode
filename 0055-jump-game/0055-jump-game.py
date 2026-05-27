class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 全局的能跳到的最远位置，初始值为0
        mr = 0
        
        # loop over (i,nums[i])
        for i,num in enumerate(nums):
            if mr<i: # 永远无法到达最右端
                return False
            # update mr
            mr = max(mr,i+num) # 比较当前下标能跳的最远位置和全局能跳的最远位置
        return True