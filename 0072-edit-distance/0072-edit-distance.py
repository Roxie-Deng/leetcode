class Solution:
    def minDistance(self, s: str, t: str) -> int:
        if s == t:
            return 0
        # dp[i][j]: s[:i]变为t[:j]的最小距离
        # dp[i][j] = dp[i-1][j-1], if s[i-1]==t[j-1]
        # if s[i-1]!=t[j-1]，对s的操作有以下三种情况：
        # 多了 ->delete s[i-1]: 再算s[:i-1]到t[:j]的距离，dp[i-1][j]
        # 少了 ->insert t[j-1]: 再算s[:i]到t[:j-1]的距离，dp[i][j]
        # 错了 -> replace: 两边指针都往前挪，再算s[:i-1]到t[:j-1]的距离
        # 
        rows,cols = len(s),len(t)
        # 构建(r+1)*(c+1)的表格
        dp = [[0]*(cols+1) for _ in range(rows+1)]

        # 填充表格
        for i in range(rows+1):
            dp[i][0] = i
        for i in range(cols+1):
            dp[0][i] = i
            
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if s[r-1] == t[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1+min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])
        return dp[rows][cols]
        # O(rc);O(rc)