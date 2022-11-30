class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        prefix = 0
        for num in nums:
            prefix += num
            count[prefix % k] += 1
    
        res = count[0]
        for i in range(k):
            n = count[i]
            res += n * (n-1) // 2
        return res