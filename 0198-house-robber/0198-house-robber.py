class Solution:
    def rob(self, nums: List[int]) -> int:
        # 抢完第n户（按编程索引）的最大值：f(n) = max(f(n-1),f(n-2)+nums[n]), 2<=n<=len(nums)-1;f(n)=max(nums[0],nums[1]),n=1;f(n)= nums[0], n = 0
        # 重复子问题 -> DP
        # @cache
        # def dfs(n):
        #    if n == 0:
        #        return nums[0]
        #    elif n == 1:
        #        return max(nums[0],nums[1])
        #    else:
        #        return max(dfs(n-1),dfs(n-2)+nums[n])
        # return dfs(len(nums)-1)
        # O(n);O(n)

        # 递推解法：递归变数组 dfs(i) -> f[i]
        # 记忆化搜索会访问 dfs(−2) 和 dfs(−1)，在 f 数组的前面插入两个 0，把 f 数组整体往右偏移 2 位
        # f = [0]*(len(nums)+2)
        # for i,x in enumerate(nums):
        #    f[i+2] = max(f[i+1],f[i]+x)
        # return f[-1]
        # O(n);O(n)

        # 空间优化
        a = b = 0
        for x in nums:
            a, b = b, max(b,a+x)
        return b
        # O(n);O(1)
