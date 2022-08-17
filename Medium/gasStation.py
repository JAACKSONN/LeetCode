class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First compute the difference array
        # loop through the difference array until we find our first positive value
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start