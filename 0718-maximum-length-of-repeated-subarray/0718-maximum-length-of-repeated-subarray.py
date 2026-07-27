class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # brutal: 两边所有子数组，是否有相等的，并取长度最大的
        # 类似于LCS: 用dp[i][j] 表示以nums[i-1]和nums[i-2]结尾的 maximum length of repeated subarray

        m,n = len(nums1), len(nums2)
        # 初始化表格
        dp = [[0]*(n+1) for _ in range(m+1)]
        longest = 0

        # dp 的第一行和第一列一定是0

        # 填充表格
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    longest = max(longest,dp[i][j])
        return longest
        # O(mn);O(mn)