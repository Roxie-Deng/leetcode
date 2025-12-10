class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0

        for p in prices:
            min_price = min(p, min_price)
            max_diff = max(p-min_price, max_diff)

        return max_diff