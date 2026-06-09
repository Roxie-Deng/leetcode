class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 不同路径；求最值-> dp
        # f(i) = f(i-1)+1, if nums[i]>nums[j] for j in range(i)
        # f(i) = f(i-1), if nums[i]<=nums[j] for j in range(i)
        # f(i) = 1, i=0

        @cache
        def dfs(i):
            # 递推： dfs(i) = max(dfs(j))+1,如果没有任何j满足则就是1
            res = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    res = max(res,dfs(j))
            return res+1

        return max(dfs(i) for i in range(len(nums))) # 所有位置的最大值
        
        # 状态数：n；非递归操作量：n
        # O(n^2)
        # 递归深度:n; 缓存大小:n
        # O(n)