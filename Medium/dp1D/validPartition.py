class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        twos = nums[-1] == nums[-2]
        if len(nums) == 2:
            return twos
        dp1, dp2, dp3 = False, False, True
        if twos:
            dp1 = True
        for i in range(len(nums) - 3, -1, -1):
            new = False
            if nums[i] == nums[i + 1] == nums[i + 2] or nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2:
                new = new or dp3
            if nums[i] == nums[i + 1]:
                new = new or dp2
            dp3, dp2, dp1 = dp2, dp1, new

        return dp1
 