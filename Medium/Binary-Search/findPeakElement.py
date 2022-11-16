# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            left = nums[mid - 1] if mid > 0 else float("-inf")
            right = nums[mid + 1] if mid + 1 < len(nums) else float("-inf")
            
            if nums[mid] > left and nums[mid] > right:
                return mid
        
            elif right >= left:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1