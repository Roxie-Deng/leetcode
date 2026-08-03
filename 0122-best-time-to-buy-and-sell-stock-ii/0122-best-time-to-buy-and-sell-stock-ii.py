class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 问的是最优解，且存在明确的状态转移关系
        # f(i) = f(i-1)， if prices[i] <= prices[i-1]
        # f(i) = f(i-1) + prices[i]-prices[i-1]
        # DP 问题

        '''
        n = len(prices)
        dp = [0] *(n+1)

        for i in range(1,n):
            cur_pro = prices[i] - prices[i-1]
            if cur_pro <= 0:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i] + cur_pro

        return dp[n]
        # O(n);O(n)
        '''

        # 继续优化：可以不用数组记录状态，而用一个变量
        cur_max = 0
        n = len(prices)

        for i in range(1,n):
            cur_pro = prices[i] - prices[i-1]
            # if cur_pro <= 0: cur_max维持原状
            if cur_pro > 0:
                cur_max += cur_pro
        return cur_max
        # O(n);O(1)
            