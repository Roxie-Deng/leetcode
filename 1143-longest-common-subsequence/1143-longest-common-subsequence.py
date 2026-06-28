class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: 
            return len(text1)
        
        # dp[i][j] 代表text1 [0,i] 和 text2[0,j] 的longest
        # dp[i][j] = dp[i-1][j-1] +1, if text1[i]==text2[j]
        # if text1[i]!=text2[j]，扔掉其中一个，比较dp[i-1][j],dp[i][j-1]取最大值

        # 创建数组(m+1)*(n+1)
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        # 填充数组
        for i,c1 in enumerate(text1):
            for j,c2 in enumerate(text2):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j] + 1 #从(1,1)开始
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
        
        return dp[m][n]
        # O(mn);O(mn)