class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
#         if len(cost) == 2:
#             return min(cost[0], cost[1])
        
#         dp = [0] * (len(cost) - 1)
        
#         dp[0] = cost[0]
#         dp[1] = cost[1]
        
#         for i in range(2, len(cost) - 1):
#             dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
#         print(dp)
#         return min(dp[-1], dp[-2] + cost[-1])
        
    
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])