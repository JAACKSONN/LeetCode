class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0; //pointer that moves to the right by 1 each time
        int j = 0; //pointer that keeps track of the beginning of the window.
        
        int max = 0;
        
        HashSet<Character> set = new HashSet<>();
        
        while(i < s.length()){
            if(!set.contains(s.charAt(i))){
                set.add(s.charAt(i));
                max = Math.max(max, set.size());
                i++;
            }
            else{
                set.remove(s.charAt(j));
                j++;
            }
        }
        return max;
    }     
}