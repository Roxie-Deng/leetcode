class Solution:
    def numSquares(self, n: int) -> int:
        # f(n) = 1, n is a perfect square nums
        # f(n) = min(f(n-j**2)+1, for j in range[1,math.isqrt(n)])
        @cache
        def dfs(n):
            root = math.isqrt(n)
            if root*root == n:
                return 1
            else:
                min_cnt = n
                for j in range(1,root+1):
                    min_cnt = min(min_cnt,dfs(n-j*j)+1)
                return min_cnt 
        return dfs(n)
        