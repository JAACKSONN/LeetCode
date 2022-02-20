class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempMax = nums[0]
        maxStore = []
        maxStore.append(tempMax)
        n = len(nums)
        for i in range (1, n):
            maxStore.append(max(maxStore[i - 1] + nums[i], nums[i]))
            if maxStore[i] > tempMax:
                tempMax = maxStore[i]
        return tempMax