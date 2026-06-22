class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(m-1,n-1) = f(m-1-1,n-1)+f(m-1,n-1-1)
        # f(r,c) = f(r-1,c)+f(r,c-1)
        # 重复子问题 -> 递归
        '''
        @cache
        def dfs(r,c): # 代表从(0,0)走到(r,c)经历的不同路径
            if r<0 or c<0:
                return 0
            if r==0 or c==0:
                return 1 # 只有从一个方向来，只有一条unique path
            return dfs(r-1,c)+dfs(r,c-1)
        
        return dfs(m-1,n-1)

        # 使用了记忆化递归（@cache）后，状态数为 m*n，每个状态只计算一次，所以时间复杂度为 O(m×n)。空间上，缓存本身占 O(m×n)，递归栈深度为 O(m+n)，因此总空间复杂度为 O(m×n)。
        '''
        # 1:1翻译为dp迭代
        # dp[r][c] = dp[r-1][c]+dp[r][c-1] 从(0,0)到达(r,c)经历的unique paths
        # 新建m行n列表格
        dp = [[0]*n]*m 

        # 第一行和第一列均为1
        dp[0] = [1]*n
        for i in range(1,m):
            dp[i][0] = 1
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        
        return dp[m-1][n-1]
        # O(mn);O(mn)