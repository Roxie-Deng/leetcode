class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Flood fill: 利用沉岛（将访问过的陆地置为0）代替 visited 集合，降低空间复杂度
        rows, cols = len(grid), len(grid[0])
        cnt = 0 # num of islands

        def dfs(r: int,c: int): # 将坐标为(r,c)的点和它的上下左右四个点都改为0
            if r<0 or r>= rows or c<0 or c>=cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)

        # 遍历所有点
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1 
                    dfs(r,c) # 从这个点开始把整块岛淹掉
        return cnt

        # 时间：1. 状态总数*每个状态的操作复杂度 -> O(r*c)*O(1)。 or 2. 外层循环嵌套次数 + 递归函数执行总次数(即 if grid[r][c] == "1"通过的次数) -> O(r*c)*O(r*c)
        #只有首次访问一个格子时，才会继续递归，其余情况不会继续递归。
        # O(r*c)
        # 空间：横向递归深度r，纵向递归深度c, 额外内存:原地修改 -> O(r*c)