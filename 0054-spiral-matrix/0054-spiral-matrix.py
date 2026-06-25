class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        size = m*n
        ans = []
        i,j,di = 0,-1,0 # 从(0,-1)开始向右走。因为先移动，再添加
        directions = [(0,1),(1,0),(0,-1),(-1,0)]# di=0，1，2，3分别代表右下左上
        # n,m-1,n-1,m-2,n-2,...
        # 第一步步长为n, 每次顺时针旋转90度的步长可以看作行列交换并减1
        # step = n
        # m,n = n,m-1

        while len(ans)<size:
            dx,dy = directions[di] 
            for _ in range(n): # n代表步长的范围
                i += dx
                j += dy
                ans.append(matrix[i][j])
            # 转弯
            di = (di+1)%4
            n,m = m,n 
            n -= 1 
        return ans
    # O(mn);O(1)

