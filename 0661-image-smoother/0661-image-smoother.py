class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # 获取矩阵的行数和列数
        rows = len(img)
        cols = len(img[0])
        # 【列表推导式】生成新矩阵存储结果，以0填充
        res = [[0]*cols for _ in range(rows)]

        # 遍历矩阵中每一个格子
        for r in range(rows):
            for c in range(cols):
                total = 0 # 存储合法邻居的数值和
                cnt = 0 # 存储合法邻居的个数

                # 遍历以(r,c)为中心的3*3区域，坐标范围是(r-1,c-1)到(r+1,c+1)
                for nr in range(r-1,r+2):
                    for nc in range(c-1,c+2):
                        # 检查邻居格子是否在合法范围内,索引范围[0,rows-1],[0,cols-1]
                        if 0<=nr<rows and 0<=nc<cols:
                            total += img[nr][nc]
                            cnt += 1
                res[r][c] = total//cnt
        return res