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
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)
        return quickSelect(0, len(nums) - 1)
                    