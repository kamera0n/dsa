class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = prices[0]
        maxProfit = 0
        for price in prices:
            minNum = min(minNum, price)
            maxProfit = max(maxProfit, price - minNum)
        return maxProfit
