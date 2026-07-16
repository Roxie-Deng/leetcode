class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brutal: 对于每一个num，遍历它剩下数组得到len_LIS，再比较
        # 求最值：当前直接决定 vs 需要尝试多种可能性，本题显然是后者
        # dp[i] 代表以nums[i]结尾的最长序列
        # dp[i] = max(dp[j])+1 for all j<i and nums[j]<nums[i]
        # dp[0] = 1
        # return max(dp)

        n = len(nums)
        dp = [1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
        # O(n^2);O(n)