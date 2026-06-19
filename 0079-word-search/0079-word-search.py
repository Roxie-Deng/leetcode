class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0]) 
        n = len(word)

        def dfs(r,c,i) -> bool: # 匹配(r,c)和word[i]
            if i == n: # 所有下标都找到了
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            # 由于不可重复且需要恢复现场
            temp = board[r][c]
            board[r][c] = "0"

            # 寻找下一个字母
            found = (dfs(r-1,c,i+1) or dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1, i+1)) # 只要有一条路返回True就行

            board[r][c] = temp # 恢复现场

            return found 

        # 遍历所有格子作为起点
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0): # 进入递归，返回True or False
                        return True # any起点返回了True最终答案就是True
        return False

        # O(r*c*4^n),n为len(word)
        # O(n),递归深度