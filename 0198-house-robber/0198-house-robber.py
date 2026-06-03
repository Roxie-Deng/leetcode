class Solution:
    def rob(self, nums: List[int]) -> int:
        # 抢完第n户（按编程索引）的最大值：f(n) = max(f(n-1),f(n-2)+nums[n]), 2<=n<=len(nums)-1;f(n)=max(nums[0],nums[1]),n=1;f(n)= nums[0], n = 0
        # 重复子问题 -> DP
        @cache
        def dfs(n):
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[0],nums[1])
            else:
                return max(dfs(n-1),dfs(n-2)+nums[n])
        
        return dfs(len(nums)-1)