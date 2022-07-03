class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        res = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res