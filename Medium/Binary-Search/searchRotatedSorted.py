class Solution:
    def search(self, nums: List[int], target: int) -> int:
#          First find the pivot
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            curr = nums[mid]
            
            if curr == target:
                return mid
            
#             means we are in the left hand side of the array
            if nums[lo] <= curr:
                if target > curr or target < nums[lo]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if target < curr or target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        return -1
                
            
            
            
             
    