class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 重叠子问题
        # pt[r][0] = 1, pt[r][-1] = 1
        # pt[2][1] = pt[1][0] + pt[1][1], pt[3][1] = pt[2][0]+pt[2][1], pt[3][2]=pt[2][1]+pt[2][2]
        # 规律：pt[r][rc] = pt[r-1][rc-1] + pt[r-1][rc] 
        # r范围[0,numRows-1],rc范围[0,r]

        pt = [] # list of rows,; 题目所给限制: 1 <= numRows <= 30

        for r in range(0,numRows):
            row = [1]*(r+1) # 空列表不能直接赋值，不能写成pt[r]
            for c in range(1,r):
                row[c] = pt[r-1][c-1] + pt[r-1][c]
            pt.append(row)
        return pt
