class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            # intervals are overlapping
            if start <= prevEnd:
                prevEnd = max(prevEnd, end)
                continue
            else:
                output.append([prevStart, prevEnd])
                prevStart = start
                prevEnd = end
                
        output.append([prevStart, prevEnd])
        return output
                
            