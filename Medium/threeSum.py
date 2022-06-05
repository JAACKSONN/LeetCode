class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            Sum = 0 - nums[i]
            lo, hi = i + 1, len(nums) - 1
            
            while lo < hi:
                currSum = nums[lo] + nums[hi]
                if Sum == currSum:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]: hi -= 1
                    lo += 1
                    hi -= 1
                elif currSum < Sum:
                    lo += 1
                else:
                    hi -= 1
        
        return res