class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 皇后可以攻击同行，同列，同斜线
        # 每一行/列上均只能有一个皇后
        # 同斜线上也只能有一个皇后：↗ r+c恒等，↘ r-c恒等
        # 一行一行放置，在每一行依次尝试每一列，安全就放置
        # 但如果下一行所有列都放不了，就撤销 -> 回溯，递归

        # 初始化已经出现过的 col, r+c, r-c
        cols = set()
        diag1 = set()
        diag2 = set()

        # 初始化棋盘
        board = [['.'] * n for _ in range(n)]
        ans = [] # 字符串数组容器

        def backtrack(row): # 正在处理第row行（可能还处理row+1行）
            # 1. 终止：找到一个有效解
            if row == n:
                # 将board的每一行从数组转化为字符串
                ans .append(["".join(row) for row in board])
                return # 返回上一级探索其他可能
            
            # 2. 尝试每一列
            for col in range(n):
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue # 如果不安全，跳过这个位置
                    
                # 放置皇后并记录危险集合
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)

                # 3. 尝试下一行
                backtrack(row+1)

                # 4. 恢复现场（可能已经有很多个递归栈，一步一步往上恢复）
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)
        
        backtrack(0)
        return ans
        # O(n!)每一行可选列逐步递减
        # O(n^2)棋盘