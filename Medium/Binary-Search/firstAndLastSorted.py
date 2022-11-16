class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs (leftBias):
            lo, hi = 0, len(nums) - 1
            i = -1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                curr = nums[mid]
                if (curr < target):
                    lo = mid + 1
                elif (curr > target):
                    hi = mid - 1
                else:
                    if leftBias:
                        i = mid
                        hi = mid - 1
                    else:
                        i = mid
                        lo = mid + 1
            return i
        
        return(bs(True), bs(False))
                
        
        
                