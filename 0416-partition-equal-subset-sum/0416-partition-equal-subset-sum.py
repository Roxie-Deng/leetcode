class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s//2
        if target in nums:
            return True
        if max(nums) > target:
            return False
        n = len(nums)

        @cache
        def dfs(i,cur_sum):
            if cur_sum == target:
                return True
            if i == n or cur_sum > target:
                return False
            return dfs(i+1,cur_sum+nums[i]) or dfs(i+1,cur_sum) # 选或不选
        return dfs(0,0) 
        # 状态数*非递归操作数：O(n*target*1)
        # 递归深度+缓存大小: O(n+n*target)