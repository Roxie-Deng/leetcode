class Solution:
    def climbStairs(self, n: int) -> int:
        # 计算不同路径->dp
        # f(i) = f(i-1)+f(i-2) 变形斐波那契额数列；状态转移方程；递归->dp
        if n <= 2:
            return n
        a = 1
        b = 2
        for _ in range(3,n+1): 
            a,b = b,a+b # 滚动更新
        return b
