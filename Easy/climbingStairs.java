class Solution {
    public int climbStairs(int n) {
        int [] prevArray = new int [n+1];
        prevArray[0] = 1;
        prevArray[1] = 1;

        for(int i = 2; i <= n; i++){
            prevArray[i] = prevArray[i - 1] + prevArray[i-2];
        }
        
        return prevArray[n];
    }
}