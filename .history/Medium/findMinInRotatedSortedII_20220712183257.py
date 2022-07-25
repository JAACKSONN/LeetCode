class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        
        res = nums[0]
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
                
            mid = l + (r - l) // 2
            res = min(res, nums[mid], nums[l])
            if nums[r] == nums[l]:
                r-=1
                l+=1
            elif nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res
            

        