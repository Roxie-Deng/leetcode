class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        '''
        # r,c [0,n-1]
        # (0,n-1)是新的原点
        # matrxi[i][0] for i（倒叙）是新的x轴
        # matrxi[n] 是新的y轴
        # (r,c),c到n-1的距离的距离就是到新y轴的距离，r到0的距离就是到新x轴的距离
        # matrix[r][c] -> matrix[n-1-c][r]

        # (2,2), n= 4 -> (1,2)
        m = [[0]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                m[r][c] = matrix[n-1-c][r]

        matrix[:] = m #如果要用额外矩阵，应该把 m 的内容复制回 matrix 指向的原始对象
        '''

        # 原地修改
        # matrix[r][c] -> matrix[n-1-c][r]会改变没访问过的值
        # 想办法进行两元素的交换
        # y=x上的元素都会留在本来的行，沿这条对角线进行交换，再把每一行reverse
        for r in range(n):
            for c in range(r+1,n): # 注意只能遍历上三角，遍历全局会交换两次就回去了
                matrix[r][c],matrix[c][r] = matrix[c][r],matrix[r][c]
        
        for row in matrix:
            row.reverse()
        # O(n^2);O(1)