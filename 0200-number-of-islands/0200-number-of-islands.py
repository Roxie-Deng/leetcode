class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 in (r,c) : (r-1,c),(r+1,c),(r,c-1),(r,c+1) -> 0 直到不再碰到1

        rows = len(grid)
        cols = len(grid[0])
        cnt = 0 

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0": # 返回条件
                return False
            
            grid[r][c] = "0"
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r,c)
        
        return cnt

        # O(rc);O(rc)