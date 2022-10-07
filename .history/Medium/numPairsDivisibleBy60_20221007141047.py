# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         remainders = {}
#         res = 0
#         for num in time:
#             mod = num % 60
#             remainders[mod] = remainders.get(mod, 0) + 1
        
#         for remainder in remainders:
#             comp = (60 - remainder) % 60
#             if comp == remainder:
#                 res += (remainders[remainder] * (remainders[remainder] - 1))
#             else:
#                 if comp in remainders:
#                     res += (remainders[remainder] * remainders[comp])
#         return res // 2
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            if t % 60 == 0: # check if a%60==0 && b%60==0
                ret += remainders[0]
            else: # check if a%60+b%60==60
                ret += remainders[60-t%60]
            remainders[t % 60] += 1 # remember to update the remainders
        return ret
                
                