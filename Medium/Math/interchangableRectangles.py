class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        
        for width, height in rectangles:
            ratio = height / width
            if ratio in count:
                count[ratio] += 1
            else:
                count[ratio] = 1
        
        res = 0
        
        for ratio in count:
            n = count[ratio]
            if n > 1:
              res += (n * (n-1)) // 2
        return res
                