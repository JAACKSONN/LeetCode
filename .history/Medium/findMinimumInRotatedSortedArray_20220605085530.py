class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0 , len(nums) - 1
        
        Min = nums[0]
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if nums[mid] >= nums[0]:
                lo = mid + 1
            else:
                Min = min(nums[mid], Min)
                hi = mid - 1
        return Min
        