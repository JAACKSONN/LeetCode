class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     return nums[-k]
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heapq.heapify(nums)
    #     while len(nums) > k:
    #         heapq.heappop(nums)
    #     return nums[0]
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, left = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left += 1
            nums[left], nums[r] = nums[r], nums[left]
            if left == k:
                return nums[left]
            elif left < k:
                return quickSelect(left + 1, r)
            else:
                return quickSelect(l, left - 1)
        return quickSelect(0, len(nums) - 1)
                    