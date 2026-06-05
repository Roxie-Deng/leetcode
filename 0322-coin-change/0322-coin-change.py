class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 最优子结构；重复子问题 -> dp
        # f(amount) = min_f(amount-coin)+1, for coin in coins
        # f(0) = 0
        @lru_cache(None)
        def dfs(n):
            if n == 0:
                return 0
            elif n < 0:
                return -1
            else:
                min_cnt = float('inf')
                for c in coins:
                    sub = dfs(n-c)
                    if sub != -1:
                        min_cnt = min(min_cnt, sub+1)
                return min_cnt if min_cnt != float('inf') else -1
        return dfs(amount)
