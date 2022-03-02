class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        if (n == 1){
            return s;
        }

        boolean dp [][] = new boolean[n][n];        
        
        //do it for length 1
        int maxLength = 1;
        int startIndex = 0;
        for(int i = 0; i < n; i++){
            dp[i][i] = true;
        }
        
        //do it for length 2
        for(int i = 0; i < n - 1; i++){
            if(s.charAt(i) == s.charAt(i+1)){
                dp[i][i+1] = true;
                maxLength = 2;
                startIndex = i;
            }
        }
        //first loop gives length of substring
        for(int i = 3; i <= n; i++){
            //second loop gives starting index and loops until the ending index
            for(int start = 0; start < n - i + 1; start++){
                int end = start + i - 1;
                if(dp[start + 1][end - 1] == true){
                    if(s.charAt(start) == s.charAt(end)){
                        maxLength = i;
                        startIndex = start;
                        dp[start][end] = true;
                    }
                }
            }
        }
        return s.substring(startIndex, startIndex + maxLength);
    }
}
