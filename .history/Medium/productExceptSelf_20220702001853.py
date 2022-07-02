class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pre = 1
#         Compute the prefix list
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        
#         Compute postfix list
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res
# #         Compute the prefix list

#         for i in range(len(nums)):
#             if i == 0:
#                 prefix[0] = nums[0]
#             else:
#                 prefix[i] = nums[i] * prefix[i - 1]
# #         Compute postfix list
#         for i in range(len(nums) - 1, -1, -1):
#             if i == len(nums) - 1:
#                 postfix[len(nums) - 1] = nums[len(nums) - 1]
#             else:
#                 postfix[i] = nums[i] * postfix[i + 1]
        
#         res = [0] * len(nums)
        
#         for i in range(len(nums)):
#             if i == 0:
#                 prefixVal = 1
#             else:
#                 prefixVal = prefix[i - 1]
#             if i == len(nums) - 1:
#                 postfixVal = 1
#             else:
#                 postfixVal = postfix[i + 1]
#             res[i] = prefixVal * postfixVal
        
#         return res
        
            
        
        