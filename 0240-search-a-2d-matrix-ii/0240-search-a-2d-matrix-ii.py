class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        if target<matrix[0][0] or target>matrix[rows-1][cols-1]:
            return False # O(1)
        
        # 行列之间没有绝对顺序，找一个起点，每种if只能往一个方向走
        # 从右上角开始，matrix[r][c] < target, 只能往下走
        # matrix[r][c] > target, 只能往左走

        r = 0
        c = cols-1
        while r<rows and c>=0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
        # 最远走到左下角O(r+c); O(1)