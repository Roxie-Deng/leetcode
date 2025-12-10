class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Multiple transactions allowed; think of a line chart, only take upward segments
        max_profit = 0
        n = len(prices)

        for i in range(1,n): # if n == 0, will skip
            if prices[i]-prices[i-1] > 0:
                max_profit += prices[i]-prices[i-1]
        
        return max_profit
        # O(n); O(1)