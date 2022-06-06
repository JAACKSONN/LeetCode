class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = len(nums) + 1
        l, r = 0, 1
        currSum = nums[0]
        while l < len(nums):
            if currSum >= target:
                minSize = min(r- l, minSize)
                currSum -= nums[l]
                l+=1
            elif r < len(nums):
                currSum += nums[r]
                r += 1
            else:
                break
        
        
        return minSize if minSize < len(nums) + 1 else 0