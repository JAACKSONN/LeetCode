class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, curSubset, total):
            if i >= len(candidates) or total > target:
                return
            
            if total == target:
                res.append(curSubset.copy())
                return
            
            curSubset.append(candidates[i])
            backtrack(i, curSubset, total + candidates[i])
            curSubset.pop()
            backtrack(i + 1, curSubset, total)
        
        backtrack(0, [], 0)
        return res
            