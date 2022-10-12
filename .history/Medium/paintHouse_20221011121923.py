class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev0, prev1, prev2 = costs[0][0], costs[0][1], costs[0][2]
        for r in range(1, len(costs)):
            prev0, prev1, prev2 = min(prev1, prev2) + costs[r][0], min(prev0, prev2) + costs[r][1], min(prev0, prev1) + costs[r][2]
        return min(prev0, prev1, prev2)
                