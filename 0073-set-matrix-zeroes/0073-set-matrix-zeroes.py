class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0 on (r,c), (r, 0-n) 和 (0-m, c)都变为0
        # 想象成Excel，用第一行和第一列做标题行/标题列标记0
        # 所以第一行/第一列都要最后处理，避免混淆是表内信息和表头信息
        rows, cols = len(matrix),len(matrix[0])
        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any(matrix[r][0]==0 for r in range(rows))

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, rows): # 处理行，看第一列上的0（跳过第一行（0,0））
            if matrix[r][0] == 0:
                matrix[r] = [0]*cols
        for c in range(1, cols): # 处理列，看第一行上的0（跳过第一列(0,0))
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        
        # 处理第一行/列本身
        if first_row_has_zero:
            matrix[0] = [0]*cols
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
        # O(rc);O(1)
       