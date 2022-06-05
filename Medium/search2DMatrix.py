class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        
        top, bottom = 0, m - 1
        while top <= bottom:
            row = top + (bottom - top) // 2
            if target > matrix[row][-1]:
                top += 1
            elif target < matrix[row][0]:
                bottom -= 1
            else:
                break
        if not (top <= bottom):
            return False
        
        row = top + (bottom - top) // 2
        
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if (matrix[row][mid] == target):
                return True
            elif (matrix[row][mid] > target):
                hi = mid - 1
            else:
                lo = mid + 1
        return False

# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         left, right = 0, m * n - 1
        
#         while left <= right:
#             piv = (left + right) // 2
#             piv_x, piv_y = piv // n, piv % n
            
#             if matrix[piv_x][piv_y] == target:
#                 return True
#             elif matrix[piv_x][piv_y] < target:
#                 left = piv + 1
#             else:
#                 right = piv - 1
        
#         return False