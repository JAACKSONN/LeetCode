class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo = i + 1
            hi = n - 1
            while lo < hi:
                sum = -nums[i]
                if nums[lo] + nums[hi] == sum:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1 
                    lo+=1
                    hi-=1
                elif nums[lo] + nums[hi] < sum:
                    lo+=1
                else:
                    hi-=1
            
        
        return ans