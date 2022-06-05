class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        
        half = (len(A) + len(B))//2
        
        if len(B) < len(A):
            A, B = B, A
        
        lo, hi = 0, len(A) - 1
        while True:
            i = lo + (hi - lo) // 2
            j = (half - 1) - (i + 1)
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i + 1 < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j + 1 < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                hi = i - 1
            else:
                lo = i + 1
        return -1
                