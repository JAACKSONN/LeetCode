/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int min = Integer.MAX_VALUE;
    public void helper(TreeNode root, int count){
        if(root == null) return;
        
        if(root.left == null && root.right == null)
            if(count < min) min = count;
        
        helper(root.left, count + 1);
        helper(root.right, count + 1);
    }
    
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        helper(root, 1);
        return min;
    }
}