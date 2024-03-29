class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)
        
        for start, end, inc in updates:
            res[start] += inc
            res[end + 1] -= inc
        
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        res.pop()
        return res