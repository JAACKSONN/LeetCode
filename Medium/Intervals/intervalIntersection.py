# https://leetcode.com/problems/interval-list-intersections/
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aPtr = 0
        bPtr = 0
        if len(A) < 1 or len(B) < 1:
            return []
        res = []
        while aPtr < len(A) and bPtr < len(B):
            a1, a2 = A[aPtr]
            b1, b2 = B[bPtr]
            if a1 <= b2 and b1 <= a2:
                res.append([max(a1, b1), min(a2,b2)])
            if a2 <= b2:
                aPtr+=1
            else:
                bPtr+=1
        return res