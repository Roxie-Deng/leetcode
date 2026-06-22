class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 到达(r,c)的min sum f[r][c] = min(f[r-1][c],f[r][c-1]) + grid[r][c]
        # 重复子问题 -> dp

        '''
        # 新建一个m行n列的空白表格
        m,n = len(grid),len(grid[0])
        dp = [[0] * n for _ in range(m)] # dp = [[0]*n]*m如果用*m会复制第一行整个列表引用

        dp[0][0] = grid[0][0]

        # 第一行 dp[0][c] = dp[0]的前缀和
        # 第一列同理
        for c in range(1,n):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        for r in range(1,m):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        
        # 可以从(1,1)逐渐向下计算
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = grid[r][c] + min(dp[r-1][c],dp[r][c-1])
        return dp[m-1][n-1]
        # O(mn);O(mn)
        '''

        # 继续优化，没必要存而二维数组，不断地覆盖每一行就行
        m,n = len(grid),len(grid[0])

        dp = [0]*n
        dp[0] = grid[0][0]
        # 填充第一行
        for c in range(1,n):
            dp[c] = dp[c-1]+grid[0][c]
        
        for r in range(1,m): # 从第二行开始
            dp[0] += grid[r][0]
            for c in range(1,n):
                dp[c] = grid[r][c] + min(dp[c],dp[c-1]) # (1,1) dp[1]:上一行同列旧值(0,1)，dp[0]:左侧值(1,0)
        return dp[-1]

        # O(mn);O(n)