class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brutal: O(n^2)
        # record min, max_profit
        min_buy = prices[0]
        max_profit = 0
        n = len(prices)

        for p in prices:
            min_buy = min(min_buy,p)
            max_profit = max(max_profit, p-min_buy)
        
        return max_profit
        # O(n);O(1)

