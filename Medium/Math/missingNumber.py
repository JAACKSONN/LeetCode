# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += (i + 1) - nums[i] # deals with overflow instead of gauss formula
        return res