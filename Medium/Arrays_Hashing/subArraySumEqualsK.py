class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = curr_sum = 0
        mp = {0 : 1}
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in mp:
                count += mp[curr_sum - k]
            mp[curr_sum] = mp.get(curr_sum, 0) + 1
        return count

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefix = [0] * (len(nums) + 1)
#         for i in range(1, len(nums) + 1):
#             prefix[i] = prefix[i - 1] + nums[i - 1]
        
#         count = 0
#         print(prefix)
#         for i in range(len(nums)):
#             for j in range(i, len(nums)):
#                 if prefix[j + 1] - prefix[i] == k:
#                     count += 1
#         return count
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             curr_sum = 0
#             for j in range(i, len(nums)):
#                 curr_sum += nums[j]
#                 if curr_sum == k:
#                     count += 1
#         return count
