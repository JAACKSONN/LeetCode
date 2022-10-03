\# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        ROWS, COLS = binaryMatrix.dimensions()
        
        rightBoundary = COLS - 1
        foundOne = False
        for row in range(ROWS):
            # now going to do binary search for the left most 1
            l, r = 0, rightBoundary
            if rightBoundary == 0:
                return 0
            if binaryMatrix.get(row, rightBoundary) == 0:
                continue
            while l <= r:
                mid = l + (r - l) // 2
                
                val = binaryMatrix.get(row, mid)
                if val == 1:
                    foundOne = True
                    rightBoundary = mid
                    r = mid - 1
                else:
                    l = mid + 1
        return rightBoundary if foundOne else -1