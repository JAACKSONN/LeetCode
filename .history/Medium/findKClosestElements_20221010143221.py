class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # first, find index of where x would be sorted in the arr
        res = []
        def find_index():
 
            # Lower and upper bounds
            start = 0
            end = len(arr) - 1

            # Traverse the search space
            while start<= end:

                mid =(start + end)//2

                if arr[mid] == x:
                    return mid

                elif arr[mid] < x:
                    start = mid + 1
                else:
                    end = mid-1

            # Return the insert position
            return end + 1
        
        index = find_index()
        l, r = index - 1, index
        
        while k and l >= 0 and r < len(arr):
            a, b = arr[l], arr[r]
            
            if abs(a - x) <= abs(b - x):
                res.append(a)
                l-=1
            else:
                res.append(b)
                r += 1
            k -= 1
        while k:
            if l < 0:
                b = arr[r]
                res.append(b)
                r += 1
                k-=1
            else:
                a = arr[l]
                res.append(a)
                l -= 1
                k -= 1
        return sorted(res)
                
        
        
        