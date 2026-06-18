class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # flood fill
        # 最短路径，多个扩散源，状态同步变化 -> BFS; 队列保证逐层扩散的遍历顺序 queue, popleft
        rows, cols = len(grid), len(grid[0])
        fresh = 0 # 新鲜橘子数量
        rq = deque() # 腐烂橘子队列

        # 遍历统计新鲜橘子数量并将腐烂橘子入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2: # 使用else减少进入第二种情况判断的次数
                    rq.append((r,c)) # 保存坐标

        if fresh == 0: # [[0]]
            return 0

        # 层序遍历
        ans = -1
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while rq: # 有腐烂橘子
            ans += 1
            for _ in range(len(rq)): # 把当前队列中的所有烂橘子拿出来感染一遍
                r,c = rq.popleft() 
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0<= nc <cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        rq.append((nr,nc))
        
        return ans if fresh == 0 else -1

        # O(rc)
        # 队列空间：每一层/每一分钟正在腐烂的橘子：O(rc)