# https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(curSum):
            if curSum in dp:
                return dp[curSum]
            if curSum > target:
                return 0
            if curSum == target:
                return 1
            dp[curSum] = 0
            for num in nums:
                dp[curSum] += dfs(curSum + num)
            return dp[curSum]
        return dfs(0)