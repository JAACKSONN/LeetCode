class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = prices[0]
        
        for i in range(len(prices)):
            profit = prices[i] - minPrice
            maxProf = max(profit, maxProf)
            minPrice = min(minPrice, prices[i])
            
        return maxProf
            